# 📂 data/loader.py
import os
import json
import pandas as pd

def ler_csv_seguro(path):
    try:
        # tenta padrão (vírgula)
        df = pd.read_csv(path)

        # se só tiver 1 coluna → provavelmente separador errado
        if len(df.columns) == 1:
            df = pd.read_csv(path, sep=";")

        return df

    except Exception as e:
        print(f"❌ Erro ao ler CSV {path}: {e}")
        return pd.DataFrame()

# 🔧 Normalização de colunas
def normalizar_colunas(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )
    return df

# 📂 FUNÇÃO PRINCIPAL PARA CARREGAR DADOS
def carregar_dados():
    try:
        print("📂 Carregando arquivos do ambiente...")

        base_path = os.path.dirname(os.path.abspath(__file__))

        # ------------------------
        # TRANSAÇÕES
        # ------------------------
        path_t = os.path.join(base_path, "transacoes.csv")
        transacoes = ler_csv_seguro(path_t)
        transacoes = normalizar_colunas(transacoes)

        print("🧾 Colunas transações:", list(transacoes.columns))

        # ------------------------
        # HISTÓRICO
        # ------------------------
        path_h = os.path.join(base_path, "historico_atendimento.csv")
        historico = ler_csv_seguro(path_h)
        historico = normalizar_colunas(historico)

        print("📞 Colunas histórico:", list(historico.columns))

        # ------------------------
        # JSONs
        # ------------------------
        with open(os.path.join(base_path, "produtos_financeiros.json"), encoding="utf-8") as f:
            produtos = json.load(f)

        with open(os.path.join(base_path, "perfil_investidor.json"), encoding="utf-8") as f:
            perfil = json.load(f)

        print("✅ Dados carregados com sucesso!\n")

        return transacoes, historico, produtos, perfil

    except Exception as e:
        print("❌ ERRO:", e)
        return pd.DataFrame(), pd.DataFrame(), [], {}
       
