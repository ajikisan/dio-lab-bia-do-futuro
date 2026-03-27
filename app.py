# 🌐 app.py — Interface Gradio

import gradio as gr

# 🔁 importa o orquestrador
from main import responder

# 📊 gráficos + placeholder
from ui.graficos import (
    grafico_atendimento_com_historia,
    grafico_transacoes_com_historia,
    capivara_placeholder
)

# 📂 dados globais
from data.loader import transacoes, historico


# 🏰 Mensagem inicial
mensagem_inicial = """
🏰 Bem-vindo ao Reino das Moedas!
Eu sou a Capivara Financeira, guardiã divertida que transforma o dinheiro em aventuras mágicas.
💰 Seu tesouro cresce nos rios das entradas, enfrenta dragões das saídas e segue protegido pelas muralhas rumo às conquistas épicas.
Sempre ao seu lado, sem substituir o valor das conversas humanas.
"""


# 🔧 Wrappers (IMPORTANTE)
def grafico_atendimento_ui():
    fig, narrativa, audio, _ = grafico_atendimento_com_historia(historico)
    return fig, narrativa, audio


def grafico_transacoes_ui():
    fig, narrativa, audio, _ = grafico_transacoes_com_historia(transacoes)
    return fig, narrativa, audio


# 🎨 Interface
with gr.Blocks() as app:

    gr.Markdown("# Capivara Financeira no Reino das Moedas")

    with gr.Row():

        # 💬 CHAT
        with gr.Column(scale=2):

            chatbot = gr.Chatbot(
                value=[{"role": "assistant", "content": mensagem_inicial}],
                type="messages",
                height=400
            )

            msg = gr.Textbox(
                placeholder="Pergunte sobre suas moedas...",
                lines=1
            )

            with gr.Row():
                enviar = gr.Button("Enviar")
                limpar = gr.Button("Limpar")

            audio_output = gr.Audio(label="Áudio", autoplay=True)
            grafico_output = gr.Plot(value=capivara_placeholder())

            # 🚀 envio
            enviar.click(
                responder,
                [msg, chatbot],
                [msg, chatbot, grafico_output, audio_output]
            )

            msg.submit(
                responder,
                [msg, chatbot],
                [msg, chatbot, grafico_output, audio_output]
            )

            # 🧹 limpar
            def limpar_chat():
                return "", [{"role": "assistant", "content": mensagem_inicial}], capivara_placeholder(), None

            limpar.click(
                limpar_chat,
                [],
                [msg, chatbot, grafico_output, audio_output]
            )

        # 📊 VISUAL
        with gr.Column(scale=1):

            gr.Markdown("## 📊 Visualizações")

            btn_atendimento = gr.Button("Gráfico de Atendimento")
            btn_transacoes = gr.Button("Gráfico de Transações")

            narrativa_output = gr.Textbox(lines=8)

            btn_atendimento.click(
                grafico_atendimento_ui,
                [],
                [grafico_output, narrativa_output, audio_output]
            )

            btn_transacoes.click(
                grafico_transacoes_ui,
                [],
                [grafico_output, narrativa_output, audio_output]
            )


# 🚀 rodar
if __name__ == "__main__":
    app.launch(share=True)