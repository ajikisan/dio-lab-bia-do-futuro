# 🤖 IA — Geração de respostas

import os
import requests
from transformers import pipeline


# 🚀 Modelo local
try:
    gerador_local = pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-125M"
    )
except Exception as e:
    print("⚠️ Erro ao carregar modelo local:", e)
    gerador_local = None


# 🎭 SYSTEM PROMPT - Personalidade da Inteligência Artificial
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


# 🌐 API HuggingFace (opcional)
HF_TOKEN = os.environ.get("HF_TOKEN")
API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
} if HF_TOKEN else {}


def gerar_resposta_ia(pergunta, contexto=""):
    if not HF_TOKEN:
        return None

    try:
        prompt = f"""
{SYSTEM_PROMPT}

Contexto:
{contexto}

Pergunta:
{pergunta}

Resposta:
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


# 🧠 Função principal - Pipeline de Respostas
def gerar_resposta(
    pergunta,
    dados=None,
    executar_func=None,
    buscar_contexto_func=None,
    vector_db=None,
    usar_token=False
):

    dados = dados or {}

    try:
        # =============================
        # 🔎 1 Regras Determinísticas
        # =============================
        if executar_func:
            resp = executar_func(pergunta, dados)
            if resp and "não reconhecida" not in str(resp).lower():
                return resp

        # =============================
        # 🔎 Contexto Semântico RAG
        # =============================
        contexto = dados.get("contexto", "")

        if not contexto and buscar_contexto_func and vector_db:
            contexto = buscar_contexto_func(pergunta, vector_db)

        # =============================
        # 🌐 IA externa opcional
        # =============================
        if usar_token:
            resp = gerar_resposta_ia(pergunta, contexto)
            if resp:
                return resp

        # =============================
        # 🤖 Modelo local fallback
        # =============================
        if gerador_local:
            prompt = f"""
{SYSTEM_PROMPT}

Contexto:
{contexto}

Pergunta:
{pergunta}

Resposta:
"""

            resultado = gerador_local(
                prompt,
                max_new_tokens=120,
                do_sample=True,
                temperature=0.7
            )

            texto = resultado[0]["generated_text"]

            # limpeza
            if "Resposta:" in texto:
                texto = texto.split("Resposta:")[-1]

            return texto.strip()

        return "⚠️ Nenhum modelo disponível."

    except Exception as e:
        print("❌ Erro IA:", e)
        return "⚠️ A Guardiã encontrou um obstáculo mágico."