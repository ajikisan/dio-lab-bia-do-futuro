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