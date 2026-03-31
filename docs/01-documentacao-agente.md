# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas têm dificuldade em acompanhar seus gastos e entender para onde o dinheiro está indo.
O processo tradicional de controle financeiro é visto como chato, complicado e pouco acessível, o que desmotiva
usuários iniciantes ou pessoas que não têm familiaridade com termos bancários.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente **Capivara Financeira** é um assistente inteligente que:
- Recebe perguntas em linguagem natural relacionadas às finanças pessoais;
- Acessa dinamicamente os dados locais de transações, histórico, produtos e perfil;
- Responde com explicações claras, contextualizadas e facilmente compreensíveis;
- Gera **gráficos e áudio** quando pertinente;
- Registra todas as interações para avaliação posterior.

Diferente de soluções estáticas, o agente **não fixa os dados no system prompt** — ele consulta os datasets conforme a necessidade de cada pergunta.


**Exemplo de resposta:**  
📊 Renda: 5000.0 | Gastos: 2488.9 | Comprometimento: 49.8% → Situação: bom



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
  🏰 Bem-vindo ao Reino das Moedas! Eu sou a Capivara Financeira, guardiã divertida que transforma o dinheiro em aventuras mágicas. 💰 Seu tesouro cresce nos rios das entradas, enfrenta dragões das saídas e segue protegido pelas muralhas rumo às conquistas épicas. Sempre ao seu lado, sem substituir o valor das conversas humanas.

- **Confirmação:**  
  📜 A Guardiã, serena à beira do rio, aguarda sua pergunta para abrir os pergaminhos mágicos do Reino das Moedas e revelar os segredos do seu tesouro.

- **Erro/Limitação:**  
  📩 Para suporte humano:
✨ Saudações, viajante do Reino das Moedas! ✨

   Em sua jornada pelas riquezas e mistérios financeiros, saiba que não caminha só.  
   
   Eu, a Guardiã Digital das Moedas, estarei sempre ao seu lado para iluminar o caminho.  

   E, se precisar de algo além das minhas forças digitais, posso abrir o portal até a guardiã humana que deu vida a esta aventura.

   Quando as dúvidas surgirem como sombras, procure pela criadora Mirian Ajiki Molicawa.  

   Assim, seus passos permanecerão firmes diante dos desafios do destino. 🤝  
   
   🔗 [LinkedIn](https://www.linkedin.com/in/mirian-ajiki-molicawa/)
   
   💻 [GitHub](https://github.com/ajikisan)

## Arquitetura

### Diagrama
```mermaid


flowchart TD
    A[Usuario] --> T1[Pergunta em texto] --> B[Interface Web Gradio Colab]
    B --> T2[Clique botao Grafico ou Audio] --> B1[Botao Grafico Audio]
    B --> T3[Envio da pergunta] --> C[Agente Backend]
    C --> D{Regras ou RAG IA}
    D --> E[Execucao de Regras]
    D --> F[IA LLM]
    F --> G[Base de Conhecimento CSV dados]
    G --> F
    E --> T4[Resultado regras] --> C
    F --> T5[Resultado IA] --> C
    C --> T6[Resposta texto grafico audio] --> B
    B --> T7[Exibe resultado] --> A
    B1 --> T8[Aciona grafico audio] --> C







```


### Componentes

| Componente                   | Função                                                                |
| ---------------------------- | --------------------------------------------------------------------- |
| Interface Web (Gradio/Colab) | Recebe perguntas e exibe respostas, gráficos e áudio                  |
| Botões de Gráfico / Áudio    | Disparam consultas específicas ao backend                             |
| Agente / Backend             | Coordena o fluxo de decisão: Regras ou RAG/IA                         |
| Decisão Regras / RAG-IA      | Determina a forma de gerar a resposta                                 |
| Execução de Regras Locais    | Respostas padrões rápidas ou cálculos simples                         |
| IA / LLM                     | Gera respostas contextualizadas e interage com a base de conhecimento |
| Base de Conhecimento         | Dados carregados localmente (transações, histórico, produtos, perfil) |
| Usuário                      | Interage com perguntas e botões                                       |

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
- [X] Não acessa dados bancários reais
- [X] Não substitui consultoria financeira profissional
- [X] Não garante precisão em cálculos complexos (trabalha apenas com dados mockados).
- [X] Não recomenda investimentos ou produtos financeiros específicos.
- [X] Não interpreta informações fora dos arquivos fornecidos (JSON/CSV)
- [X] Não responde sobre temas fora do escopo de finanças pessoais simuladas
