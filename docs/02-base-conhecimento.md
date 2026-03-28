# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Capivara Financeira e suas ações|
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | A Capivara relembra conversas anteriores e dá continuidade às aventuras financeiras, mostrando o que "se lenbra" do usuário e mantém o fio da narrativa.|
| `perfil_investidor.json` | JSON | A Capivara interpreta o perfil (conservador, moderado, arrojado) e adapta sua história, sugerindo caminhos compatíveis com o estilo do cliente.|
| `produtos_financeiros.json` | JSON | A Capivara apresenta opções de produtos como personagens de uma história, explicando de forma lúdica quais se encaixam melhor no perfil investidor |
| `transacoes.csv` | CSV | A Capivara transforma cada gasto em metáforas divertidas: "Chef da Alimentação", o "Motorista do Transporte", o "Artista do Lazer", criando uma narrrativa sobre quem está dominnado o reino finaneeiro. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

No momento, os dados permanecem mockados e não foram alterados.
Cada arquivo é usado apenas para simulação lúdica da Capivara Financeira.

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.
- Os arquivos **JSON/CSV mockados** ficam armazenados no Google Drive.  
- No início da sessão no **Google Colab**, o Drive é montado e os arquivos são lidos com `pandas`.  
- Exemplo:
  ```python
  from google.colab import drive
  drive.mount('/content/drive')

  import pandas as pd
  df = pd.read_csv('/content/drive/MyDrive/capivara-financeira/transacoes.csv')
  ```



### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados não ficam fixos no system prompt.

Eles são consultados dinamicamente a cada interação:


data/transacoes.csv

**Transações Financeiras**
```
data	descricao	categoria	valor	tipo
2025-10-01	Salário	receita	5000.00	entrada
2025-10-02	Aluguel	moradia	1200.00	saida
2025-10-03	Supermercado	alimentacao	450.00	saida
2025-10-05	Netflix	lazer	55.90	saida
2025-10-07	Farmácia	saude	89.00	saida
2025-10-10	Restaurante	alimentacao	120.00	saida
2025-10-12	Uber	transporte	45.00	saida
2025-10-15	Conta de Luz	moradia	180.00	saida
2025-10-20	Academia	saude	99.00	saida
2025-10-25	Combustível	transporte	250.00	saida
```

data/produtos_financeiros.json

**Produtos Financeiros**
```
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```
data/perfil_investidor.json

**Perfil do Investidor**
```
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}
```
data/historico_atendimento.csv

**Histórico de Atendimentos**
```
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim...
```

O agente lê o CSV/JSON.

Resume os valores por categoria.

Constrói uma resposta narrativa (ex.: “Chef da Alimentação gastou 200 moedas”).

Isso garante que a Capivara Financeira só fale com base nos dados disponíveis, evitando alucinações.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.


data/transacoes.csv

**Transações Financeiras**
```
data	descricao	categoria	valor	tipo
2025-10-03	Supermercado	alimentacao	450.00	saida
2025-10-05	Netflix	lazer	55.90	saida
```

"Oi, eu sou a Capivara Financeira! Vi que o Chef da Alimentação gastou 450 moedas no Supermercado e o Artista do Lazer usou 55 moedas em Streaming. Quem será que está dominando seu reino financeiro hoje?"

