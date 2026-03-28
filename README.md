<<<<<<< HEAD
<p align="center">
  <img src="assets/capivara_webp.webp" width="300"/>
</p>

<h1 align="center">🏰 Capivara Financeira</h1>
<p align="center">IA no Reino das Moedas</p>

Uma assistente financeira inteligente com narrativa lúdica, que combina **Regras + RAG + IA generativa** para analisar dados, responder perguntas e gerar insights sobre a vida financeira do usuário.

---

## 🎯 Objetivo

Criar uma experiência interativa que:

* 📊 Analisa transações financeiras
* 🧠 Utiliza busca semântica (RAG)
* 🤖 Gera respostas com IA
* 🎭 Apresenta resultados com narrativa gamificada
* 🔊 Converte respostas em áudio
* 📈 Exibe gráficos interativos

---

## 🧠 Arquitetura do Projeto

O sistema segue uma arquitetura modular baseada em camadas:

```bash
capivara-financeira/
│
├── app.py                  # Interface com Gradio
├── main.py                 # Orquestrador principal
│
├── core/                   # Lógica de negócio
│   ├── intencoes.py        # Detecção de intenção (regex)
│   ├── regras.py           # Regras e análises financeiras
│   ├── rag.py              # RAG (FAISS + embeddings)
│   ├── ia.py               # Integração com IA (local + API)
│   ├── audio.py            # Geração de áudio (gTTS)
│
├── data/                   # Dados
│   ├── loader.py
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── produtos_financeiros.json
│   ├── perfil_investidor.json
│
├── ui/
│   ├── graficos.py         # Gráficos + narrativas
│
├── utils/
│   ├── normalizacao.py
│   ├── constantes.py
│
├── assets/
│   └── capivara_webp.webp
│
└── requirements.txt
```

---

## ⚙️ Como funciona (Fluxo)

A resposta do sistema segue 3 camadas:

1. ⚡ **Regras (rápido)**

   * Regex + lógica determinística

2. 🔎 **RAG (contexto)**

   * Busca semântica com FAISS
   * Base: transações, histórico, produtos, perfil

3. 🤖 **IA (fallback)**

   * HuggingFace API ou modelo local
   * Geração de resposta natural

---

## 🧩 Tecnologias utilizadas

* Python
* Pandas
* Matplotlib
* Gradio
* LangChain
* FAISS
* Sentence Transformers
* Transformers (HuggingFace)
* gTTS (Text-to-Speech)

---

## 🚀 Como executar (Local)

### 1. Clone o repositório

```bash
git clone https://github.com/ajikisan/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
python app.py
```

---

## ☁️ Executar no Google Colab

1. Faça upload do projeto (zip ou GitHub)
2. Instale dependências:

```python
!pip install -r requirements.txt
```

3. Execute:

```python
!python app.py
```

---

## 💡 Diferenciais do Projeto

✔️ Arquitetura modular profissional
✔️ IA híbrida (Regras + RAG + Generativa)
✔️ Busca semântica com FAISS
✔️ Interface interativa com Gradio
✔️ Narrativa gamificada (UX diferenciada)
✔️ Geração de áudio (TTS)
✔️ Visualização de dados

---

## 🎭 Experiência do Usuário

O sistema transforma finanças em uma jornada:

* 💰 Entradas → “rios de moedas”
* 🐉 Saídas → “tributos aos dragões”
* 🛡️ Reserva → “baú encantado”
* 🎯 Metas → “profecias do oráculo”

---

## 🔒 Considerações

* O sistema não acessa dados reais sensíveis
* Respeita boas práticas de segurança
* Utiliza dados simulados para demonstração

---

## 👩‍💻 Autora

**Mirian Ajiki Molicawa**

* 💼 LinkedIn: https://www.linkedin.com/in/mirian-ajiki-molicawa/
* 💻 GitHub: https://github.com/ajikisan

---

## 📌 Status do Projeto

🚧 Em evolução — melhorias contínuas em IA, UX e performance.

---

## ⭐ Contribuição

Sinta-se à vontade para abrir issues ou contribuir com melhorias!

---
