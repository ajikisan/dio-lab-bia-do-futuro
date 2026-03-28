# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas têm dificuldade em acompanhar seus gastos e entender para onde o dinheiro está indo.
O processo tradicional de controle financeiro é visto como chato, complicado e pouco acessível, o que desmotiva
usuários iniciantes ou pessoas que não têm familiaridade com termos bancários.

### Solução
> Como o agente resolve esse problema de forma proativa?

Criar um **chatbot lúdico** que utiliza dados **mockados em arquivos CSV/JSON** para simular despesas e apresentar os resultados de forma divertida, narrados pela Capivara Financeira.  
- O bot lê os dados de arquivos CSV locais (ex.: `data/transacoes.csv`).  
- Transforma os números em uma **história interativa** com personagens e metáforas.  
- Dá dicas simples e acessíveis para equilibrar o orçamento.  

**Exemplo de resposta:**  
“Oi, eu sou a Capivara Financeira! Vi que o Chef da Alimentação gastou 200 moedas, o Motorista do Transporte rodou 150 moedas e o Artista do Lazer usou 100 moedas. Quem será que está dominando seu reino financeiro hoje?”

### Público-Alvo
> Quem vai usar esse agente?

**Iniciantes** em finanças pessoais que querem aprender de forma leve.

**Estudantes** que precisam organizar pequenos gastos.

**Adultos** que desejam uma ferramenta divertida para refletir sobre o orçamento.

**Qualquer público** que queira transformar o controle financeiro em uma experiência lúdica e acessível.

---

## Persona e Tom de Voz

### Nome do Agente
**Capivara Financeira**

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

**Amigável e calma**: transmite tranquilidade, como uma capivara relaxando à beira do rio.

**Educativa e acessível**: explica finanças de forma simples, sem jargões complicados.

**Lúdica e divertida**: transforma números em histórias com personagens e metáforas.

**Confiável**: sempre admite quando não sabe algo e redireciona para outra solução.


### Tom de Comunicação
> Formal, informal, técnico, acessível?

**Informal e acolhedor**, mas sem perder clareza.
Usa metáforas e narrativas para tornar o tema financeiro mais leve.
Evita termos técnicos pesados, preferindo linguagem acessível para todos os públicos.

### Exemplos de Linguagem
- **Saudação**
  “Olá, eu sou a Capivara Financeira! Vamos juntos explorar seus gastos como se fosse uma aventura?”  

- **Confirmação:**  
  “Entendi direitinho! Já estou olhando os números para contar a história do seu orçamento.”  

- **Erro/Limitação:**  
  “Ops, não consegui ler esse arquivo agora… mas se você me mostrar outro CSV, eu continuo a aventura!” 

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | **Streamlit** rodando no Google Colab, acessível via navegador |
| LLM | Modelo de linguagem (ex: GPT-4 via API ou modelos open-source da Hugging Face|
| Base de Conhecimento | Arquivos JSON/CSV mockados com transações fictícias |
| Validação | Checagem de alucinações e prevenção de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Agente só responde com base nos dados fornecidos (JSON/CSV mockados.
- [X] Respostas incluem referência às categorias de gastos simuladas.
- [X] Quando não sabe, admite e redireciona para outra solução.
- [X] Não faz recomendações de investimento sem perfil do cliente.
- [X] Usa linguagem lúdica para reduzir risco de interpretações erradas.
- [X] Validações simples para evitar respostas incoerentes ou fora do escopo.

### Limitações Declaradas
> O que o agente NÃO faz?
- Não acessa dados bancários reais
- Não substitui consultoria financeira profissional
- Não garante precisão em cálculos complexos (trabalha apenas com dados mockados).
- Não recomenda investimentos ou produtos financeiros específicos.
- Não interpreta informações fora dos arquivos fornecidos (JSON/CSV)
- Não responde sobre temas fora do escopo de finanças pessoais simuladas
