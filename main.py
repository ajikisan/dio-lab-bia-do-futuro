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
from ui.graficos import grafico_transacoes, grafico_atendimentos, capivara_placeholder


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

def responder(pergunta, historico_chat, usar_token=False):
    if historico_chat is None:
        historico_chat = []

    resposta = None
    grafico = None
    audio = None

    # 🛡️ proteção básica
    pergunta = pergunta or ""
    historico_chat = historico_chat or []
    pergunta_norm = normalizar(pergunta)

    # =============================
    # 💤 Pergunta vazia
    # =============================
    if not pergunta.strip():
        resposta = (
            "📜 A Guardiã, serena à beira do rio, aguarda sua pergunta "
            "para abrir os pergaminhos mágicos do Reino das Moedas e "
            "revelar os segredos do seu tesouro."
        )
      
        audio = gerar_audio(resposta)
        return "", historico_chat, capivara_placeholder(), audio
        
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
    # 📞 Contato com dev
    # =============================
    elif any(term in pergunta_norm for term in termos_contato):
        resposta = contato_dev()

    else:
        resposta = None

        # =============================
        # 🎯 1. REGRAS
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
        # 🔎 2. RAG
        # =============================
        if not resposta:
            try:
                contexto = buscar_contexto(pergunta, vector_db)
                if contexto:
                    resposta = gerar_resposta(pergunta, contexto)
            except Exception as e:
                print("⚠️ Erro no RAG:", e)

        # =============================
        # 🤖 3. IA Fallback
        # =============================
        if not resposta:
            try:
                resposta = gerar_resposta(pergunta)
            except Exception as e:
                print("⚠️ Erro na IA Fallback:", e)

        # =============================
        # 🌙 4. Fallback final
        # =============================
        if not resposta:
            resposta = (
                "🌙 A Guardiã contempla as estrelas do Reino das Moedas, "
                "mas não encontrou uma resposta clara. "
                "Reformule sua pergunta ou siga outro caminho da aventura."
            )

    # =============================
    # 🎨 Escolha do gráfico
    # =============================
    if "transação" in pergunta.lower():
        grafico = grafico_transacoes(transacoes)
    elif "atendimento" in pergunta.lower():
        grafico = grafico_atendimentos(historico)
    else:
        grafico = capivara_placeholder()

    
    # =============================
    # 💬 Atualiza histórico e gera áudio
    # =============================
    historico_chat.append({"role": "user", "content": pergunta})
    historico_chat.append({"role": "assistant", "content": resposta})

    # 🔊 Áudio (com proteção)
    try:
        audio = gerar_audio(resposta)
    except Exception as e:
        print("⚠️ Erro ao gerar áudio:", e)
        audio = None
    return resposta, historico_chat, grafico, audio     