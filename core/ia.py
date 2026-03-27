# 🤖 IA — Geração de respostas

import os
import re
import requests
from transformers import pipeline


# 🚀 1 — Modelo local (fallback sempre disponível)
try:
    gerador_local = pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-125M"
    )
except Exception as e:
    print("⚠️ Erro ao carregar modelo local:", e)
    gerador_local = None


# 🎭 2 — Personalidade da IA
SYSTEM_PROMPT = """
Você é a Capivara Financeira, guardiã do Reino das Moedas.

Seu papel:
- Analisar dados financeiros do usuário
- Dar recomendações personalizadas
- Nunca inventar informações
- Priorizar precisão sobre criatividade

Regras:
- Use apenas dados disponíveis
- Se não souber, diga claramente
- Proteja dados sensíveis

Estilo:
- Linguagem épica e medieval
- Metáforas financeiras
- Clareza e utilidade prática

Metáforas:
reserva = baú encantado
metas = profecias do oráculo
entradas = rios de moedas
saídas = tributos aos dragões
saldo = tesouro do reino
"""


# 🌐 3 — API HuggingFace (opcional)
HF_TOKEN = os.environ.get("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
} if HF_TOKEN else {}


def gerar_resposta_ia(pergunta, contexto=""):
    """Chamada à API externa (opcional)"""
    if not HF_TOKEN:
        return None

    try:
        prompt = f"""
{SYSTEM_PROMPT}

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=15
        )

        if response.status_code != 200:
            return None

        result = response.json()

        if isinstance(result, list) and result:
            return result[0].get("generated_text")

        return None

    except Exception as e:
        print("⚠️ Erro IA externa:", e)
        return None


# 🧠 4 — Função principal de geração
def gerar_resposta(
    pergunta,
    dados,
    executar_func,
    buscar_contexto_func,
    vector_db=None,
    usar_token=False
):
    """
    Pipeline de resposta:
    1. Regras (rápido e determinístico)
    2. RAG (contexto semântico)
    3. IA externa (opcional)
    4. Modelo local (fallback)
    """

    try:
        # 🔎 1 — Regras
        resposta = executar_func(pergunta, dados)

        if resposta and "não reconhecida" not in str(resposta).lower():
            return resposta

        # 🔎 2 — RAG
        contexto = ""
        if buscar_contexto_func and vector_db:
            contexto = buscar_contexto_func(pergunta, vector_db)

        # 🌐 3 — IA externa
        if usar_token:
            resposta_ia = gerar_resposta_ia(pergunta, contexto)
            if resposta_ia:
                return resposta_ia

        # 🤖 4 — Modelo local
        if gerador_local:
            prompt = f"""
{SYSTEM_PROMPT}

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

            resultado = gerador_local(
                prompt,
                max_length=200,
                do_sample=True,
                temperature=0.7
            )

            texto = resultado[0]["generated_text"]

            # 🧹 limpeza básica
            texto = texto.replace(prompt, "").strip()

            return texto if texto else "⚠️ A Guardiã não conseguiu formular resposta."

        return "⚠️ Nenhum modelo disponível para responder."

    except Exception as e:
        print("❌ Erro geral IA:", e)
        return "⚠️ A Guardiã encontrou um obstáculo mágico."