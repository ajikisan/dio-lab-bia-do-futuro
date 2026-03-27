# 🧠 main.py — Orquestrador principal

import os
import sys

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
from data.loader import carregar_dados

# 🧰 Utils
from utils.normalizacao import normalizar
from utils.constantes import sensivel_termos, termos_contato

# 🎨 UI
from ui.graficos import capivara_placeholder

# 📊 Carrega dados ao iniciar
try:
    transacoes, historico, produtos, perfil = carregar_dados()
except Exception as e:
    print("❌ Erro ao carregar dados:", e)
    transacoes, historico, produtos, perfil = None, None, None, None


# 🔁 FUNÇÃO PRINCIPAL (ORQUESTRADOR)
def responder(pergunta, historico_chat, usar_token=False):

    # 🛡️ proteção básica
    pergunta = pergunta or ""
    historico_chat = historico_chat or []

    pergunta_norm = normalizar(pergunta)

    # 💤 Pergunta vazia
    if not pergunta.strip():
        resposta = (
            "📜 A Guardiã, serena à beira do rio, aguarda sua pergunta "
            "para abrir os pergaminhos mágicos do Reino das Moedas e   "
            "revelar os segredos do seu tesouro."
        )

        historico_chat.append({"role": "assistant", "content": resposta})

        audio = gerar_audio(resposta)

        return "", historico_chat, capivara_placeholder(), audio

    # 👤 Salva pergunta do usuário
    historico_chat.append({"role": "user", "content": pergunta})

    # 🔒 Segurança
    if any(term in pergunta_norm for term in sensivel_termos):
        resposta = (
            "🔒 Os segredos do reino não podem ser revelados. "
            "Nem mesmo a Guardiã tem acesso a essas informações," 
            "pois estão protegidas por feitiços invioláveis."
        )

    # 📞 Contato com dev
    elif any(term in pergunta_norm for term in termos_contato):
        resposta = contato_dev()

    else:
        resposta = None

        # 🎯 1. Regras (rápido e determinístico)
        try:
            resposta = executar(pergunta, {
                "transacoes": transacoes,
                "perfil": perfil,
                "produtos": produtos
            })
        except Exception as e:
            print("⚠️ Erro nas regras:", e)

        # 🔎 2. RAG (se regras não responderam)
        if not resposta:
            try:
                contexto = buscar_contexto(pergunta)
                if contexto:
                    resposta = contexto
            except Exception as e:
                print("⚠️ Erro no RAG:", e)

        # 🤖 3. IA (fallback final)
        if not resposta:
            try:
                resposta = gerar_resposta(pergunta, usar_token=usar_token)
            except Exception as e:
                print("⚠️ Erro na IA:", e)

    # ⚠️ fallback final
    if not resposta:
        resposta = "⚠️ A Guardiã não encontrou resposta."

    # 🤖 Salva resposta
    historico_chat.append({"role": "assistant", "content": resposta})

    # 🔊 Áudio (com proteção)
    try:
        audio = gerar_audio(resposta)
    except Exception as e:
        print("⚠️ Erro ao gerar áudio:", e)
        audio = None

    return "", historico_chat, capivara_placeholder(), audio