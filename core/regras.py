# 📊 core/regras.py — FUNÇÕES ANALÍTICAS

import pandas as pd


# --- Funções auxiliares ---
def safe_get(d, key, default=None):
    """Retorna valor seguro de dicionário, mesmo se d for None"""
    return d.get(key, default) if d else default


def obter_meta_reserva(perfil):
    """Retorna (reserva_atual, valor_meta, falta)"""
    reserva_atual = safe_get(perfil, "reserva_emergencia_atual", 0)
    metas = safe_get(perfil, "metas", [])
    meta = next((m for m in metas if "reserva" in m.get("meta", "").lower()), None)

    valor_meta = safe_get(meta, "valor_necessario", 0) if meta else 0
    falta = max(valor_meta - reserva_atual, 0)

    return reserva_atual, valor_meta, falta


def calcular_transacoes(transacoes):
    """Calcula entradas, saídas e saldo"""
    if transacoes is None or transacoes.empty:
        return {
            "entradas": 0,
            "saidas": 0,
            "saldo": 0,
            "maior": 0,
            "menor": 0,
            "media": 0
        }

    df = transacoes.copy()
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    entradas = df.loc[df["tipo"] == "entrada", "valor"].sum()
    saidas = df.loc[df["tipo"] == "saida", "valor"].sum()
    saldo = entradas - saidas

    gastos = df.loc[df["tipo"] == "saida", "valor"]
    maior = gastos.max() if not gastos.empty else 0
    menor = gastos.min() if not gastos.empty else 0
    media = gastos.mean() if not gastos.empty else 0

    return {
        "entradas": entradas,
        "saidas": saidas,
        "saldo": saldo,
        "maior": maior,
        "menor": menor,
        "media": media
    }


# --- Perfil e Reserva ---
def reserva(perfil):
    try:
        reserva_atual, valor_meta, falta = obter_meta_reserva(perfil)

        if valor_meta == 0:
            return "🛡️ Nenhuma meta de reserva encontrada no reino."

        return f"🛡️ O baú encantado guarda {reserva_atual} moedas, faltam {falta} para cumprir a profecia."

    except Exception as e:
        return f"⚠️ Erro ao calcular reserva: {str(e)}"


def cliente(perfil):
    try:
        if perfil is None:
            raise ValueError("Perfil não carregado")

        idade = safe_get(perfil, "idade", "desconhecido")
        profissao = safe_get(perfil, "profissao", "desconhecido")
        perfil_usuario = safe_get(perfil, "perfil_investidor", "desconhecido")
        objetivo = safe_get(perfil, "objetivo_principal", "desconhecido")
        patrimonio_total = safe_get(perfil, "patrimonio_total", 0)

        reserva_atual, valor_meta, falta = obter_meta_reserva(perfil)

        return f"""
🎯 A missão do aventureiro {safe_get(perfil,'nome','do reino')}

Segundo o pergaminho do perfil do investidor:
* Idade: {idade} anos
* Profissão: {profissao}
* Perfil: {perfil_usuario}
* Objetivo principal: {objetivo}

Situação atual do tesouro:
* 💰 Patrimônio total: {patrimonio_total}
* 🛟 Reserva de emergência atual: {reserva_atual}
* 🎯 Meta da reserva: {valor_meta}

Somente mais {falta} moedas e tua jornada será digna das lendas medievais!
"""

    except Exception as e:
        return f"⚠️ Erro ao gerar perfil do cliente: {str(e)}"


# --- Transações ---
def transacao(perfil, transacoes, metaforas):
    try:
        if perfil is None or transacoes is None or transacoes.empty:
            raise ValueError("Dados insuficientes")

        calc = calcular_transacoes(transacoes)
        reserva_atual, valor_meta, falta = obter_meta_reserva(perfil)

        perfil_tipo = safe_get(perfil, "perfil_investidor", "desconhecido")
        perfil_ludico = metaforas.get("perfil", {}).get(perfil_tipo, perfil_tipo)
        produto_chave = metaforas.get("produtos", {}).get("medio", "artefato")

        return (
            f"Em nosso reino, os {metaforas.get('entradas','ganhos')} trouxeram {calc['entradas']} moedas, "
            f"enquanto os {metaforas.get('saidas','gastos')} levaram {calc['saidas']} moedas. "
            f"O {metaforas.get('saldo','saldo')} brilha com {calc['saldo']} moedas guardadas. "
            f"O viajante, um {perfil_ludico}, segue as {metaforas.get('metas','metas')}, "
            f"que indicam acumular {valor_meta} moedas no {metaforas.get('reserva','reserva')}. "
            f"Hoje há {reserva_atual} moedas nesse baú, faltando {falta} para completar a profecia. "
            f"Artefatos como o {produto_chave} ajudam na jornada."
        )

    except Exception as e:
        return f"⚠️ Erro ao gerar narrativa: {str(e)}"


# --- Análise financeira ---
def analise_financeira(transacoes, perfil):
    try:
        if perfil is None:
            raise ValueError("Perfil não carregado")

        if transacoes is None or transacoes.empty:
            raise ValueError("Transações não carregadas")

        renda = safe_get(perfil, "renda_mensal", 0)
        calc = calcular_transacoes(transacoes)
        gastos = calc["saidas"]

        percentual = (gastos / renda * 100) if renda > 0 else 0

        if percentual < 50:
            status = "bom"
        elif percentual < 80:
            status = "atenção"
        else:
            status = "cuidado"

        return f"📊 Renda: {renda} | Gastos: {gastos} | Comprometimento: {percentual:.1f}% → Situação: {status}"

    except Exception as e:
        return f"⚠️ Erro na análise financeira: {str(e)}"


# --- Análise detalhada ---
def analisar_transacoes(transacoes, tipo="maior"):
    try:
        if transacoes is None or transacoes.empty:
            return "Não há dados de transações."

        colunas = {"tipo", "valor", "categoria"}
        if not colunas.issubset(transacoes.columns):
            return "Dados incompletos."

        df = transacoes.copy()
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

        if tipo in ["maior", "menor", "media"]:
            gastos = df[df["tipo"] == "saida"]

            if gastos.empty:
                return "Não há dados de gastos."

            if tipo == "maior":
                m = gastos.loc[gastos["valor"].idxmax()]
                return f"🏆 Maior gasto: {m['valor']} em {m['categoria']}"

            elif tipo == "menor":
                m = gastos.loc[gastos["valor"].idxmin()]
                return f"🐭 Menor gasto: {m['valor']} em {m['categoria']}"

            else:
                media = gastos["valor"].mean()
                return f"📊 Média de gastos: {media:.2f}"

        elif tipo == "total_entradas":
            entradas = df.loc[df["tipo"] == "entrada", "valor"].sum()
            return f"💰 Entradas: {entradas}"

        elif tipo == "total_saidas":
            saidas = df.loc[df["tipo"] == "saida", "valor"].sum()
            return f"💸 Saídas: {saidas}"

        return "Tipo inválido."

    except Exception as e:
        return f"⚠️ Erro: {str(e)}"


# --- Produtos ---
def explicar_produtos_ludico(produtos):
    try:
        if not produtos or not isinstance(produtos, list):
            return "Nenhum produto disponível."

        respostas = []

        for p in produtos:
            respostas.append(f"""
🪙 {p.get("nome", "Produto")}
Categoria: {p.get("categoria")}
Risco: {p.get("risco")}
Rentabilidade: {p.get("rentabilidade")}
""".strip())

        return "\n\n".join(respostas)

    except Exception as e:
        return f"⚠️ Erro: {str(e)}"


# --- Contato ---
def contato_dev():
    return """
📩 Para suporte humano:
✨ Saudações, viajante do Reino das Moedas! ✨

       Em sua jornada pelas riquezas e mistérios financeiros, saiba que não caminha só.  
       
       Eu, a Guardiã Digital das Moedas, estarei sempre ao seu lado para iluminar o caminho.  

       E, se precisar de algo além das minhas forças digitais, posso abrir o portal até a guardiã humana que deu vida a esta aventura.

       Quando as dúvidas surgirem como sombras, procure pela criadora Mirian Ajiki Molicawa.  

       Assim, seus passos permanecerão firmes diante dos desafios do destino. 🤝  
       
       🔗 [LinkedIn](https://www.linkedin.com/in/mirian-ajiki-molicawa/)
       
       💻 | [GitHub](https://github.com/ajikisan)
"""