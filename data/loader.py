# 📂 data/loader.py 

import os
import json
import pandas as pd


# 🔧 Normaliza nomes de colunas
def _normalizar_colunas(df):
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )
    return df


# 🔧 Corrige tipos de dados
def _corrigir_tipos(transacoes, historico):

    # --- TRANSACOES ---
    if transacoes is not None and not transacoes.empty:

        # valor → float
        if "valor" in transacoes.columns:
            try:
                transacoes["valor"] = (
                    transacoes["valor"]
                    .astype(str)
                    .str.replace(",", ".", regex=False)
                    .astype(float)
                )
            except Exception as e:
                print("⚠️ Erro ao converter 'valor':", e)

        # tipo → string padronizada
        if "tipo" in transacoes.columns:
            transacoes["tipo"] = (
                transacoes["tipo"]
                .astype(str)
                .str.lower()
                .str.strip()
            )

        # categoria → string padronizada
        if "categoria" in transacoes.columns:
            transacoes["categoria"] = (
                transacoes["categoria"]
                .astype(str)
                .str.lower()
                .str.strip()
            )

    # --- HISTORICO ---
    if historico is not None and not historico.empty:

        if "canal" in historico.columns:
            historico["canal"] = (
                historico["canal"]
                .astype(str)
                .str.lower()
                .str.strip()
            )

    return transacoes, historico


# 🔍 Valida estrutura mínima
def _validar_dados(transacoes, historico):

    erros = []

    if transacoes is None or transacoes.empty:
        erros.append("❌ Transações vazias")

    else:
        colunas_necessarias = {"categoria", "tipo", "valor"}
        faltantes = colunas_necessarias - set(transacoes.columns)

        if faltantes:
            erros.append(f"❌ Transações sem colunas: {faltantes}")

    if historico is None or historico.empty:
        erros.append("❌ Histórico vazio")

    else:
        if "canal" not in historico.columns:
            erros.append("❌ Histórico sem coluna 'canal'")

    return erros


# 🚀 FUNÇÃO PRINCIPAL
def carregar_dados():
    try:
        print("📂 Carregando arquivos do ambiente...")

        base_path = os.path.dirname(__file__)

        # =============================
        # 📊 CSVs
        # =============================
        transacoes_path = os.path.join(base_path, "transacoes.csv")
        historico_path = os.path.join(base_path, "historico_atendimento.csv")

        transacoes = pd.read_csv(transacoes_path, encoding="utf-8")
        historico = pd.read_csv(historico_path, encoding="utf-8")

        # Normaliza colunas
        transacoes = _normalizar_colunas(transacoes)
        historico = _normalizar_colunas(historico)

        # Corrige tipos
        transacoes, historico = _corrigir_tipos(transacoes, historico)

        # =============================
        # 📄 JSON
        # =============================
        with open(os.path.join(base_path, "produtos_financeiros.json"), encoding="utf-8") as f:
            produtos = json.load(f)

        with open(os.path.join(base_path, "perfil_investidor.json"), encoding="utf-8") as f:
            perfil = json.load(f)

        # =============================
        # 🔍 Validação
        # =============================
        erros = _validar_dados(transacoes, historico)

        if erros:
            print("\n".join(erros))
        else:
            print("✅ Dados carregados e validados com sucesso!")

        # =============================
        # 🔎 DEBUG (ajuda MUITO no Colab)
        # =============================
        print("\n🔍 DEBUG TRANSACOES")
        print(transacoes.head())
        print(transacoes.dtypes)

        print("\n🔍 DEBUG HISTORICO")
        print(historico.head())
        print(historico.dtypes)

        return transacoes, historico, produtos, perfil

    except FileNotFoundError as e:
        print("❌ Arquivo não encontrado:", e)

    except pd.errors.EmptyDataError:
        print("❌ CSV vazio ou corrompido")

    except json.JSONDecodeError:
        print("❌ Erro ao ler JSON")

    except Exception as e:
        print("❌ Erro inesperado:", e)

    # 🛟 fallback seguro (NUNCA quebra o app)
    return (
        pd.DataFrame(),
        pd.DataFrame(),
        {},
        {}
    )