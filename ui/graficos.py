# 📊 Criação de gráficos para a interface UX

import matplotlib.pyplot as plt
import os

# 🔊 Importa áudio corretamente
from core.audio import gerar_audio


# --- Caminho base do projeto ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# --- Placeholder gráfico ---
def capivara_placeholder():
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.axis("off")

    try:
        # Caminho robusto (funciona local + Colab + deploy)
        caminho_imagem = os.path.join(BASE_DIR, "assets", "capivara_webp.webp")

        img = plt.imread(caminho_imagem)
        ax.imshow(img, aspect="equal")
        ax.set_xlim(0, img.shape[1])
        ax.set_ylim(img.shape[0], 0)

    except Exception:
        ax.text(
            0.5, 0.5,
            "Capivara no reino 🐾",
            ha="center",
            va="center",
            fontsize=10
        )

    plt.tight_layout()
    return fig


# --- Gráfico de Atendimento ---
def grafico_atendimento(historico):
    fig, ax = plt.subplots(figsize=(4, 4))

    try:
        if historico is None or historico.empty:
            raise ValueError("Dados de histórico vazios")

        if "canal" not in historico.columns:
            raise KeyError("Coluna 'canal' não encontrada")

        contagem = historico["canal"].value_counts()

        ax.pie(contagem, labels=contagem.index, autopct='%1.1f%%')
        ax.set_title("Histórico de Atendimento")

    except Exception as e:
        ax.text(
            0.5, 0.5,
            f"Erro no gráfico\n{str(e)}",
            ha="center",
            va="center",
            fontsize=10
        )
        ax.axis("off")

    plt.tight_layout()
    return fig


# --- Gráfico de Transações ---
def grafico_transacoes(transacoes):
    fig, ax = plt.subplots(figsize=(7, 5))

    try:
        if transacoes is None or transacoes.empty:
            raise ValueError("Dados de transações vazios")

        colunas = {"categoria", "tipo", "valor"}
        if not colunas.issubset(transacoes.columns):
            raise KeyError(f"Colunas ausentes: {colunas - set(transacoes.columns)}")

        df = transacoes.copy()
        df["tipo"] = df["tipo"].str.lower().str.strip()

        resumo = (
            df.groupby(["categoria", "tipo"])["valor"]
            .sum()
            .unstack(fill_value=0)
        )

        resumo["entrada"] = resumo.get("entrada", 0)
        resumo["saida"] = resumo.get("saida", 0)
        resumo["saldo"] = resumo["entrada"] - resumo["saida"]

        resumo[["entrada", "saida"]].plot(kind="bar", ax=ax)

        ax.plot(
            resumo.index,
            resumo["saldo"],
            marker="o",
            linewidth=2,
            label="Saldo líquido"
        )

        ax.set_title("Entradas, Saídas e Saldo")
        ax.set_ylabel("Valor (R$)")
        plt.xticks(rotation=0)
        ax.legend()

    except Exception as e:
        ax.text(
            0.5, 0.5,
            f"Erro no gráfico\n{str(e)}",
            ha="center",
            va="center",
            fontsize=10
        )
        ax.axis("off")

    plt.tight_layout()
    return fig


# --- Narrativa Histórico ---
def narrativa_historico(historico):
    try:
        if historico is None or historico.empty:
            return "Não há histórico de atendimento."

        if "canal" not in historico.columns:
            raise KeyError("Coluna 'canal' não existe.")

        contagem = historico["canal"].value_counts()

        narrativa = "🏰 No Reino das Moedas, os guardiões atenderam assim:\n"

        for canal, valor in contagem.items():
            personagem = {
                "chat": "🧙 Mago do Chat",
                "telefone": "📞 Guardião do Telefone",
                "email": "🦉 Coruja Mensageira"
            }.get(str(canal).lower(), "🛡️ Herói Misterioso")

            narrativa += f"- {personagem}: {valor} interação(ões)\n"

        return narrativa

    except Exception as e:
        return f"Erro na narrativa: {str(e)}"


# --- Narrativa Transações ---
def narrativa_transacoes(transacoes):
    try:
        if transacoes is None or transacoes.empty:
            return "Não há dados de transações."

        for col in ["categoria", "tipo", "valor"]:
            if col not in transacoes.columns:
                raise KeyError(f"Coluna '{col}' não existe.")

        df = transacoes.copy()
        df["tipo"] = df["tipo"].str.lower().str.strip()

        resumo = (
            df.groupby(["categoria", "tipo"])["valor"]
            .sum()
            .unstack(fill_value=0)
        )

        narrativa = "💰 No Reino das Moedas, seus tesouros e gastos fluíram assim:\n"

        for categoria in resumo.index:
            entrada = resumo.loc[categoria].get("entrada", 0)
            saida = resumo.loc[categoria].get("saida", 0)
            saldo = entrada - saida

            narrativa += (
                f"- {categoria}: "
                f"entrada {entrada}, saída {saida}, saldo {saldo}\n"
            )

        return narrativa

    except Exception as e:
        return f"Erro na narrativa: {str(e)}"


# --- Gráfico + Narrativa + Áudio ---
def grafico_atendimento_com_historia(historico):
    try:
        fig = grafico_atendimento(historico)
        narrativa = narrativa_historico(historico)
        audio = gerar_audio(narrativa) if narrativa else None

        return fig, narrativa, audio, None

    except Exception as e:
        return None, None, None, str(e)


def grafico_transacoes_com_historia(transacoes):
    try:
        fig = grafico_transacoes(transacoes)
        narrativa = narrativa_transacoes(transacoes)
        audio = gerar_audio(narrativa) if narrativa else None

        return fig, narrativa, audio, None

    except Exception as e:
        return None, None, None, str(e)