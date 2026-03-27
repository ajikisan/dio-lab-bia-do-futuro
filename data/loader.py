# 📂 3 — FUNÇÃO PARA CARREGAR DADOS

def carregar_dados():
    try:

        print("📂 Carregando arquivos do ambiente...")
        # 📊 CSVs Leitura dos dados financeiros
        transacoes = pd.read_csv("transacoes.csv")
        historico = pd.read_csv("historico_atendimento.csv")

        # 📄 Leitura de arquivos JSON
        with open("produtos_financeiros.json") as f:
            produtos = json.load(f)

        with open("perfil_investidor.json") as f:
            perfil = json.load(f)

        # Retorna tudo organizado
        print("✅ Dados carregados com sucesso!")
        return transacoes, historico, produtos, perfil

    except Exception as e:
        print("❌ Erro ao carregar dados:", e)
        return None, None, None, None

# Carrega dados logo no início do sistema
transacoes, historico, produtos, perfil = carregar_dados()
