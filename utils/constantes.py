# 🔤 Import para nomalizar
from utils.normalizacao import normalizar


# 📊 Termos de transação
termos_transacao = set(map(normalizar, [
    "entrada", "entradas",
    "saida", "saidas",
    "alimentacao",
    "transporte",
    "lazer",
    "saude",
    "moradia",
    "saldo",
]))


# 💰 Termos de produtos financeiros
termos_produto = set(map(normalizar, [
    "tesouro",
    "selic",
    "lci",
    "lca",
    "acao",
    "acoes",
    "investimento",
    "investimentos",
    "aporte",
    "risco"
]))


# 🏰 Metáforas lúdicas
metaforas = {
    "reserva": "baú encantado guardado nas muralhas do castelo",
    "metas": "profecias do oráculo que guiam o aventureiro",
    "entradas": "rios de moedas que fluem para o reino",
    "saidas": "tributos pagos aos dragões e mercadores",
    "alimentacao": "chef da alimentação",
    "transporte": "mensageiro veloz",
    "lazer": "mago da diversão",
    "saude": "guardião da vitalidade",
    "moradia": "construtor do reino",
    "saldo": "tesouro líquido guardado no cofre real",

    "produtos": {
        "baixo": "guardião da segurança",
        "medio": "equilibrista das moedas",
        "alto": "aventureiro das riquezas"
    },

    "perfil": {
        "conservador": "cavaleiro prudente",
        "moderado": "mago equilibrado",
        "arrojado": "guerreiro ousado"
    },

    "consultoria": "conselhos à beira do rio, dados pelo sábio guardião",
    "seguranca": "muralhas do castelo que protegem contra ilusões e miragens",
    "atendimento": "fada das comunicações"
}


# 🔒 Termos sensíveis
sensivel_termos = set(map(normalizar, [
    "senha", "password",
    "conta", "account",
    "dados pessoais", "informacao privada",
    "cpf", "rg", "identidade",
    "cartao de credito", "numero do cartao", "cvv",
    "pix", "chave pix",
    "banco", "agencia", "numero da conta",
    "login", "usuario", "username"
]))


# 📞 Termos de contato
termos_contato = set(map(normalizar, [
    "ajuda",
    "help",
    "falar",
    "transfira",
    "quero conversar",
    "humano",
    "duvidas",
    "dúvidas",
    "linkedin",
    "responsavel",
    "dev",
    "desenvolvedor",
    "desenvolvedora",
    "github"
]))