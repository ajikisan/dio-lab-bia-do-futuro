# 📂 FUNÇÃO PARA CARREGAR DADOS
def carregar_dados():
    try:
        print("📂 Carregando arquivos do ambiente...")

        base_path = os.path.dirname(__file__)

        # =========================
        # 📊 CARREGAMENTO DOS CSVs
        # =========================
        try:
            transacoes = pd.read_csv(
                os.path.join(base_path, "transacoes.csv"),
                encoding="utf-8"
            )
        except UnicodeDecodeError:
            transacoes = pd.read_csv(
                os.path.join(base_path, "transacoes.csv"),
                encoding="latin-1"
            )

        try:
            historico = pd.read_csv(
                os.path.join(base_path, "historico_atendimento.csv"),
                encoding="utf-8"
            )
        except UnicodeDecodeError:
            historico = pd.read_csv(
                os.path.join(base_path, "historico_atendimento.csv"),
                encoding="latin-1"
            )

        # =========================
        # 🔧 NORMALIZA COLUNAS
        # =========================
        transacoes.columns = transacoes.columns.str.lower().str.strip()
        historico.columns = historico.columns.str.lower().str.strip()

        print("📊 Colunas transações:", list(transacoes.columns))
        print("📞 Colunas histórico:", list(historico.columns))

        # =========================
        # 🔍 VALIDAÇÃO DE COLUNAS
        # =========================
        colunas_transacoes = {"categoria", "tipo", "valor"}
        colunas_historico = {"canal"}

        if not colunas_transacoes.issubset(transacoes.columns):
            faltantes = colunas_transacoes - set(transacoes.columns)
            raise KeyError(f"❌ Transações sem colunas obrigatórias: {faltantes}")

        if not colunas_historico.issubset(historico.columns):
            faltantes = colunas_historico - set(historico.columns)
            raise KeyError(f"❌ Histórico sem colunas obrigatórias: {faltantes}")

        # =========================
        # 🔢 GARANTE TIPO NUMÉRICO
        # =========================
        transacoes["valor"] = pd.to_numeric(transacoes["valor"], errors="coerce")

        if transacoes["valor"].isna().any():
            print("⚠️ Atenção: existem valores inválidos na coluna 'valor' (convertidos para NaN)")

        # =========================
        # 📄 JSON
        # =========================
        with open(
            os.path.join(base_path, "produtos_financeiros.json"),
            encoding="utf-8"
        ) as f:
            produtos = json.load(f)

        with open(
            os.path.join(base_path, "perfil_investidor.json"),
            encoding="utf-8"
        ) as f:
            perfil = json.load(f)

        print("✅ Dados carregados com sucesso!")
        return transacoes, historico, produtos, perfil

    except Exception as e:
        print("❌ Erro ao carregar dados:", e)

        # fallback seguro (não quebra o app)
        return (
            pd.DataFrame(),
            pd.DataFrame(),
            {},
            {}
        )