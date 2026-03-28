# 📂 data/loader.py 
import os
import json
import pandas as pd


# 🔧 Remove lixo de merge / erros comuns
def _limpar_linhas_invalidas(df):
    if df is None or df.empty:
        return df
    
    # Remove linhas totalmente vazias   
    df = df.dropna(how="all")

    erros_excel = ["#NOME?", "#VALOR!", "#REF!", "#DIV/0!", "Erro:510"]

    # Converte tudo para string uma vez
    df = df.astype(str)

    # Remove linhas com erros de Excel
    for erro in erros_excel:
        df = df[~df.apply(lambda row: row.str.contains(erro, na=False)).any(axis=1)]

    # Remove conflitos de merge (Git)
    df = df[~df.apply(
        lambda row: row.str.contains("<<<<<<<|=======|>>>>>>>", na=False)
    ).any(axis=1)]

    return df


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

        if "valor" in transacoes.columns:
            # Remove caracteres inválidos e corrige separador
            transacoes["valor"] = (
                transacoes["valor"]
                .astype(str)
                .str.replace(",", ".", regex=False)
                .str.replace(r"[^0-9\.\-]", "", regex=True)
            )

            transacoes["valor"] = pd.to_numeric(
                transacoes["valor"],
                errors="coerce"
            )

        if "tipo" in transacoes.columns:
            transacoes["tipo"] = (
                transacoes["tipo"]
                .astype(str)
                .str.lower()
                .str.strip()
            )

        if "categoria" in transacoes.columns:
            transacoes["categoria"] = (
                transacoes["categoria"]
                .astype(str)
                .str.lower()
                .str.strip()
            )

        # Remove linhas onde valor ficou inválido
        if "valor" in transacoes.columns:
            transacoes = transacoes.dropna(subset=["valor"])

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
        # 📊 CSVs (robusto contra erro)
        # =============================
        transacoes_path = os.path.join(base_path, "transacoes.csv")
        historico_path = os.path.join(base_path, "historico_atendimento.csv")

        transacoes = pd.read_csv(
            transacoes_path,
            encoding="utf-8",
            on_bad_lines="skip"  # 🔥 ignora linhas quebradas
        )

        historico = pd.read_csv(
            historico_path,
            encoding="utf-8",
            on_bad_lines="skip"
        )

        # Limpeza pesada
        transacoes = _limpar_linhas_invalidas(transacoes)
        historico = _limpar_linhas_invalidas(historico)

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
        # 🔎 DEBUG
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

    # 🛟 fallback seguro
    return (
        pd.DataFrame(),
        pd.DataFrame(),
        {},
        {}
    )