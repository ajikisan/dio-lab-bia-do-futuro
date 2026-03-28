import pandas as pd
import json
import os

# 📂 FUNÇÃO PARA CARREGAR DADOS
def carregar_dados():
    try:
        print("📂 Carregando arquivos do ambiente...")

        base_path = os.path.dirname(__file__)

        # 📊 CSVs
        transacoes = pd.read_csv(os.path.join(base_path, "transacoes.csv"))
        historico = pd.read_csv(os.path.join(base_path, "historico_atendimento.csv"))

        # 📄 JSON
        with open(os.path.join(base_path, "produtos_financeiros.json"), encoding="utf-8") as f:
            produtos = json.load(f)

        with open(os.path.join(base_path, "perfil_investidor.json"), encoding="utf-8") as f:
            perfil = json.load(f)

        print("✅ Dados carregados com sucesso!")
        return transacoes, historico, produtos, perfil

    except Exception as e:
        print("❌ Erro ao carregar dados:", e)
        return None, None, None, None