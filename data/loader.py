import os
import json
import pandas as pd

# 🔧 Limpeza
def _limpar_linhas_invalidas(df):
    if df is None or df.empty:
        return df

    df = df.dropna(how="all")
    df = df.astype(str)

    erros_excel = ["#NOME?", "#VALOR!", "#REF!", "#DIV/0!", "Erro:510"]

    for erro in erros_excel:
        df = df[~df.apply(lambda row: row.str.contains(erro, na=False)).any(axis=1)]

    df = df[~df.apply(
        lambda row: row.str.contains("<<<<<<<|=======|>>>>>>>", na=False)
    ).any(axis=1)]

    return df


def _normalizar_colunas(df):
    df.columns = df.columns.str.lower().str.strip()
    return df


def _corrigir_tipos(transacoes, historico):

    if "valor" in transacoes.columns:
        transacoes["valor"] = (
            transacoes["valor"]
            .str.replace(",", ".", regex=False)
            .str.replace(r"[^0-9\.\-]", "", regex=True)
        )
        transacoes["valor"] = pd.to_numeric(transacoes["valor"], errors="coerce")
        transacoes = transacoes.dropna(subset=["valor"])

    return transacoes, historico


def carregar_dados():
    try:
        base_path = os.path.dirname(__file__)

        transacoes = pd.read_csv(os.path.join(base_path, "transacoes.csv"), on_bad_lines="skip")
        historico = pd.read_csv(os.path.join(base_path, "historico_atendimento.csv"), on_bad_lines="skip")

        transacoes = _limpar_linhas_invalidas(transacoes)
        historico = _limpar_linhas_invalidas(historico)

        transacoes = _normalizar_colunas(transacoes)
        historico = _normalizar_colunas(historico)

        transacoes, historico = _corrigir_tipos(transacoes, historico)

        with open(os.path.join(base_path, "produtos_financeiros.json"), encoding="utf-8") as f:
            produtos = json.load(f)

        with open(os.path.join(base_path, "perfil_investidor.json"), encoding="utf-8") as f:
            perfil = json.load(f)

        return transacoes, historico, produtos, perfil

    except Exception as e:
        print("Erro:", e)
        return pd.DataFrame(), pd.DataFrame(), {}, {}


# 🧠 RAG CORRETO
def carregar_vector_db():
    from core.rag import criar_documentos, criar_vector_db

    transacoes, historico, produtos, perfil = carregar_dados()

    docs = criar_documentos(transacoes, historico, produtos, perfil)
    vector_db = criar_vector_db(docs)

    return vector_db