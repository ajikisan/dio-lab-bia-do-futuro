# 📂 CARREGAMENTO DE DADOS

import os
import json
import pandas as pd


def carregar_dados(base_path="data"):
    """
    Carrega todos os dados do projeto (CSV + JSON)

    Args:
        base_path (str): caminho base da pasta data

    Returns:
        tuple: (transacoes, historico, produtos, perfil)
    """

    try:
        print("📂 Carregando arquivos...")

        # 📊 Caminhos
        path_transacoes = os.path.join(base_path, "transacoes.csv")
        path_historico = os.path.join(base_path, "historico_atendimento.csv")
        path_produtos = os.path.join(base_path, "produtos_financeiros.json")
        path_perfil = os.path.join(base_path, "perfil_investidor.json")

        # 📊 CSVs
        transacoes = pd.read_csv(path_transacoes, encoding="utf-8") \
            if os.path.exists(path_transacoes) else pd.DataFrame()

        historico = pd.read_csv(path_historico, encoding="utf-8") \
            if os.path.exists(path_historico) else pd.DataFrame()

        # 📄 JSONs
        produtos = []
        if os.path.exists(path_produtos):
            with open(path_produtos, encoding="utf-8") as f:
                produtos = json.load(f)

        perfil = {}
        if os.path.exists(path_perfil):
            with open(path_perfil, encoding="utf-8") as f:
                perfil = json.load(f)

        print("✅ Dados carregados com sucesso!")

        return transacoes, historico, produtos, perfil

    except Exception as e:
        print("❌ Erro ao carregar dados:", e)
        return pd.DataFrame(), pd.DataFrame(), [], {}