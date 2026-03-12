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

O agente lê o CSV/JSON.

Resume os valores por categoria.

Constrói uma resposta narrativa (ex.: “Chef da Alimentação gastou 200 moedas”).

Isso garante que a Capivara Financeira só fale com base nos dados disponíveis, evitando alucinações.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
Data, Categoria, Valor
2026-03-01, alimentacao, 200
2026-03-02, transporte, 150
2026-03-03, lazer, 100
2026-03-04, saude, 300
2026-03-05, educacao, 250

...
```
