# 🧠 main.py — Orquestrador principal

import os
import sys
import pandas as pd

# 🔧 Garante que os módulos locais funcionem
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# 📦 Core
from core.intencoes import executar
from core.rag import buscar_contexto
from core.ia import gerar_resposta
from core.audio import gerar_audio
from core.regras import contato_dev

# 📂 Data
from data.loader import carregar_dados, carregar_vector_db

# 🧰 Utils
from utils.normalizacao import normalizar
from utils.constantes import sensivel_termos, termos_contato

# 🎨 UI
from ui.graficos import (
    grafico_atendimento_com_historia,
    grafico_transacoes_com_historia,
    capivara_placeholder
)


# =============================
# 📊 Carregamento global (singleton)
# =============================
try:
    transacoes, historico, produtos, perfil = carregar_dados()
    vector_db = carregar_vector_db()
except Exception as e:
    print("❌ Erro ao carregar dados:", e)
    transacoes, historico, produtos, perfil = None, None, None, None
    vector_db = None

# =============================
# 🚀 FUNÇÃO PRINCIPAL (ORQUESTRADOR)
# =============================

def responder(pergunta="", historico_chat=None, usar_token=False, tipo_grafico=None):
    # 🛡️ proteção básica
    historico_chat = historico_chat or []
    pergunta = pergunta or ""
    pergunta_norm = normalizar(pergunta)

    resposta = None
    grafico = capivara_placeholder()
    audio = None
    narrativa_extra = None
    contexto = ""

    # =============================
    # 📊 BOTÕES DE GRÁFICO (sem pergunta)
    # =============================
    if not pergunta.strip() and tipo_grafico:
        if tipo_grafico == "transacoes":
            grafico, narrativa_extra, _, _ = grafico_transacoes_com_historia(transacoes)
        elif tipo_grafico == "atendimentos":
            grafico, narrativa_extra, _, _ = grafico_atendimento_com_historia(historico)

        resposta = "📊 Veja como está seu reino:\n\n" + (narrativa_extra or "")

        historico_chat.append({"role": "assistant", "content": resposta})
        audio = gerar_audio(resposta)

        return "", historico_chat, grafico, audio

    # =============================
    # 💤 Pergunta vazia (normal)
    # =============================
    if not pergunta.strip():
        resposta = (
            "📜 A Guardiã, serena à beira do rio, aguarda sua pergunta "
            "para abrir os pergaminhos mágicos do Reino das Moedas e "
            "revelar os segredos do seu tesouro."
        )

        historico_chat.append({"role": "assistant", "content": resposta})
        audio = gerar_audio(resposta)

        return "", historico_chat, grafico, audio

    # =============================
    # 🔒 Segurança
    # =============================
    if any(term in pergunta_norm for term in sensivel_termos):
        resposta = (
            "🔒 Os segredos do reino não podem ser revelados. "
            "Nem mesmo a Guardiã tem acesso a essas informações, "
            "pois estão protegidas por feitiços invioláveis."
        )
 

    # =============================
    # 📞 Contato
    # =============================
    elif any(term in pergunta_norm for term in termos_contato):
        resposta = contato_dev()

    else:
        # =============================
        # 🎯 REGRAS
        # =============================
        try:
            resposta = executar(
                pergunta,
                {
                    "transacoes": transacoes,
                    "historico": historico,
                    "produtos": produtos,
                    "perfil": perfil
                }
            )
        except Exception as e:
            print("⚠️ Erro nas regras:", e)

        # =============================
        # 🔎 RAG
        # =============================
        if not resposta:
            try:
                contexto = buscar_contexto(pergunta, vector_db)
                if contexto:
                    resposta = gerar_resposta(
                        pergunta,
                        {
                            "contexto": contexto,
                            "transacoes": transacoes,
                            "historico": historico,
                            "produtos": produtos,
                            "perfil": perfil
                        },
                        executar,
                        buscar_contexto,
                        vector_db,
                        usar_token
                    )
            except Exception as e:
                print("⚠️ Erro no RAG:", e)

        # =============================
        # 🤖 IA fallback
        # =============================
        if not resposta:
            try:
                resposta = gerar_resposta(
                    pergunta,
                    {
                        "contexto": contexto,
                        "transacoes": transacoes,
                        "historico": historico,
                        "produtos": produtos,
                        "perfil": perfil
                    },
                    executar,
                    buscar_contexto,
                    vector_db,
                    usar_token
                )
            except Exception as e:
                print("⚠️ Erro na IA Fallback:", e)

        # =============================
        # 🌙 Fallback final
        # =============================
        if not resposta:
            resposta = "🌙 A Guardiã não encontrou uma resposta clara."

    # =============================
    # 🎨 Gráfico opcional junto com resposta
    # =============================
    if tipo_grafico == "transacoes":
        grafico, narrativa_extra, _, _ = grafico_transacoes_com_historia(transacoes)
    elif tipo_grafico == "atendimentos":
        grafico, narrativa_extra, _, _ = grafico_atendimento_com_historia(historico)

    if narrativa_extra:
        resposta += "\n\n" + narrativa_extra

    # =============================
    # 💬 Histórico
    # =============================
    historico_chat.append({"role": "user", "content": pergunta})
    historico_chat.append({"role": "assistant", "content": resposta})

    # =============================
    # 🔊 Áudio
    # =============================
    try:
        audio = gerar_audio(resposta)
    except Exception as e:
        print("⚠️ Erro ao gerar áudio:", e)
        audio = None

    return resposta, historico_chat, grafico, audio 