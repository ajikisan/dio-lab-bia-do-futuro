<<<<<<< HEAD
# 🐾 Capivara Financeira

### Assistente Inteligente com IA, RAG e Análise Financeira

Projeto desenvolvido como parte do bootcamp da DIO com foco na construção de uma assistente inteligente para finanças pessoais, combinando:

* 🤖 Inteligência Artificial (LLMs)
* 🧠 RAG (Retrieval Augmented Generation)
* 📊 Análise de dados financeiros
* 🎨 Interface interativa com Gradio

---

## 🏰 Sobre o Projeto

A **Capivara Financeira** é uma assistente que atua como uma guardiã do "Reino das Moedas", ajudando o usuário a entender sua vida financeira de forma:

* Clara
* Interativa
* Lúdica (com narrativa medieval)

Ela analisa dados reais, responde perguntas, gera gráficos e até fala com o usuário 🎧

---

## 🚀 Funcionalidades

✅ Análise de transações financeiras
✅ Identificação de maior/menor gasto
✅ Cálculo de entradas, saídas e saldo
✅ Perfil do investidor
✅ Sugestão de produtos financeiros
✅ Sistema de intenção com regex
✅ RAG (busca semântica com FAISS)
✅ Integração com IA (Hugging Face)
✅ Geração de respostas em linguagem natural
✅ Narrativa gamificada (tema medieval)
✅ Geração de áudio (Text-to-Speech)
✅ Interface web interativa (Gradio)
✅ Visualização de dados (gráficos)

---

## 🧩 Arquitetura do Projeto

```bash
capivara-financeira/
│
├── core/
│   ├── intencoes.py        # 🔎 interpretação de perguntas
│   ├── regras.py           # 📊 lógica financeira
│   ├── rag.py              # 🧠 busca semântica (FAISS)
│   ├── ia.py               # 🤖 geração de respostas
│   ├── audio.py            # 🔊 geração de áudio
│
├── data/
│   ├── loader.py           # 📂 carregamento de dados
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── produtos_financeiros.json
│   ├── perfil_investidor.json
│
├── ui/
│   ├── graficos.py         # 📊 gráficos + narrativa
│
├── utils/
│   ├── normalizacao.py     # 🔤 normalização de texto
│   ├── constantes.py       # 🧠 termos e regras
│
├── assets/
│   ├── capivara_webp.webp  # 🖼️ imagem da interface
│
├── app.py                  # 🌐 interface Gradio
├── main.py                 # 🧠 orquestrador principal
├── requirements.txt        # 📦 dependências
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* Gradio
* LangChain
* FAISS
* Hugging Face Transformers
* Sentence Transformers
* Pandas
* Matplotlib
* gTTS (Text-to-Speech)

---

## ▶️ Como Executar Localmente

```bash
git clone https://github.com/ajikisan/dio-lab-bia-do-futuro
cd dio-lab-bia-do-futuro

pip install -r requirements.txt
python app.py
```

---

## ☁️ Como Executar no Google Colab

```python
!git clone https://github.com/ajikisan/dio-lab-bia-do-futuro.git
%cd dio-lab-bia-do-futuro

!pip install -r requirements.txt

!python app.py
```

---

## 💬 Exemplos de Perguntas

* "Qual meu maior gasto?"
* "Como está minha situação financeira?"
* "Quanto eu ganhei?"
* "Quais são meus investimentos?"
* "Me dê uma recomendação financeira"

---

## 🔒 Segurança

O sistema possui proteção contra acesso a dados sensíveis como:

* CPF
* Senhas
* Dados bancários

---

## 🧠 Diferenciais

✨ Arquitetura modular (nível produção)
✨ Integração de múltiplas camadas de IA
✨ Uso de RAG para enriquecer respostas
✨ Experiência gamificada (narrativa medieval)
✨ Interface interativa com gráficos + áudio

---

## 👩‍💻 Autora

**Mirian Ajiki Molicawa**

🔗 LinkedIn:
https://www.linkedin.com/in/mirian-ajiki-molicawa/

💻 GitHub:
https://github.com/ajikisan

---

## 📌 Status do Projeto

🚧 Em evolução

Melhorias futuras:

* Memória de conversa
* Deploy online
* Interface aprimorada
* Novos tipos de análise financeira

---

## ⭐ Contribuição

Sinta-se à vontade para contribuir ou sugerir melhorias!

---

## 🐾 Licença

Este projeto foi desenvolvido para fins educacionais.
Março/2026
=======
# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste desafio, você vai idealizar e prototipar um agente financeiro que utiliza IA Generativa para:

- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Qual problema financeiro ele resolve? (ex: consultoria de investimentos, planejamento de metas, alertas de gastos)
- **Persona e Tom de Voz:** Como o agente se comporta e se comunica?
- **Arquitetura:** Fluxo de dados e integração com a base de conhecimento
- **Segurança:** Como evitar alucinações e garantir respostas confiáveis?

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Perfil e preferências do cliente |
| `produtos_financeiros.json` | JSON | Produtos e serviços disponíveis |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** Instruções gerais de comportamento e restrições
- **Exemplos de Interação:** Cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** Como o agente lida com situações limite

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- Chatbot interativo (sugestão: Streamlit, Gradio ou similar)
- Integração com LLM (via API ou modelo local)
- Conexão com a base de conhecimento

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Sugeridas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Grave um **pitch de 3 minutos** (estilo elevador) apresentando:

- Qual problema seu agente resolve?
- Como ele funciona na prática?
- Por que essa solução é inovadora?

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
>>>>>>> 3ef24898e91f2e518ee9d85e50f798ace5b7e3b9
