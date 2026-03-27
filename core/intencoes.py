# 🎯 core/intencoes.py — DETECÇÃO DE INTENÇÃO

import re

# 🔤 utils
from utils.normalizacao import normalizar
from utils.constantes import (
    termos_transacao,
    termos_produto,
    termos_contato,
    metaforas
)

# 📊 regras de negócio
from core.regras import (
    analise_financeira,
    analisar_transacoes,
    reserva,
    cliente,
    transacao,
    explicar_produtos_ludico,
    contato_dev
)


# 🔧 Dispatcher único: regex → função
padroes = {

    r"\b(an[aá]lise(\s+financeira)?|ver\s+an[aá]lise)\b":
        lambda dados: analise_financeira(dados["transacoes"], dados["perfil"]),

    r"\bmaior\s+(gasto|despesa|custo|disp[eê]ndio)\b":
        lambda dados: analisar_transacoes(dados["transacoes"], "maior"),

    r"\b(maior\s+valor)\b":
        lambda dados: analisar_transacoes(dados["transacoes"], "maior"),

    r"\bmenor\s+(gasto|despesa|custo|disp[eê]ndio)\b":
        lambda dados: analisar_transacoes(dados["transacoes"], "menor"),

    r"\bm[eé]dia\b":
        lambda dados: analisar_transacoes(dados["transacoes"], "media"),

    r"\bentrada[s]?\b":
        lambda dados: analisar_transacoes(dados["transacoes"], "total_entradas"),

    r"\b(sa[ií]da|gasto[s]?\s+total|despesa[s]?\s+total|custo[s]?\s+total)\b":
        lambda dados: analisar_transacoes(dados["transacoes"], "total_saidas"),

    r"\b(reserva\s+financeira|aporte)\b":
        lambda dados: reserva(dados["perfil"]),

    r"\b(meta|metas)\b":
        lambda dados: reserva(dados["perfil"]),

    r"\b(perfil|quem\s+sou\s+eu|mim)\b":
        lambda dados: cliente(dados["perfil"]),

    r"\b(produto|investimento)\b":
        lambda dados: explicar_produtos_ludico(dados["produtos"]),

    r"\b(ajuda|help|falar|transfira|quero\s+conversar|humano|duvidas|linkedin|responsavel|dev|desenvolvedor|github)\b":
        lambda dados: contato_dev(),
}


# 🚀 Função principal de execução
def executar(pergunta: str, dados: dict) -> str | None:

    pergunta = normalizar(pergunta)

    # 🔎 regex direta
    for regex, func in padroes.items():
        if re.search(regex, pergunta):
            return func(dados)

    # 🧠 fallback inteligente (sem regex)
    if any(t in pergunta for t in termos_transacao):
        return transacao(
            dados["perfil"],
            dados["transacoes"],
            metaforas
        )

    if any(t in pergunta for t in termos_produto):
        return explicar_produtos_ludico(dados["produtos"])

    # ❌ nenhuma intenção reconhecida
    return None