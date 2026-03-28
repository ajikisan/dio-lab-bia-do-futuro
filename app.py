# 🌐 app.py — Interface Gradio
import gradio as gr

from main import responder

from ui.graficos import (
    grafico_atendimento_com_historia,
    grafico_transacoes_com_historia,
    capivara_placeholder
)

from data.loader import carregar_dados, carregar_vector_db

# 📂 Carrega dados
transacoes, historico, produtos, perfil = carregar_dados()

# 🧠 Carrega RAG corretamente
vector_db = carregar_vector_db()

#🏰 Mensagem inicial
mensagem_inicial = """
🏰 Bem-vindo ao Reino das Moedas!
Eu sou a Capivara Financeira, guardiã divertida que transforma o dinheiro em aventuras mágicas.
💰 Seu tesouro cresce nos rios das entradas, enfrenta dragões das saídas e segue protegido pelas muralhas rumo às conquistas épicas.
Sempre ao seu lado, sem substituir o valor das conversas humanas.
"""

# 🔧 Wrappers gráficos
def grafico_atendimento_ui():
    fig, narrativa, audio, _ = grafico_atendimento_com_historia(historico)
    return fig, narrativa, audio

def grafico_transacoes_ui():
    fig, narrativa, audio, _ = grafico_transacoes_com_historia(transacoes)
    return fig, narrativa, audio

# 🎯 Wrapper do responder COM RAG
def responder_ui(msg, chat):
    from core.rag import buscar_contexto

    buscar_contexto_func = lambda q: buscar_contexto(q, vector_db)

    return responder(
        msg,
        chat,
        transacoes=transacoes,
        historico=historico,
        produtos=produtos,
        perfil=perfil,
        buscar_contexto_func=buscar_contexto_func
    )

# 🎨 Interface
with gr.Blocks() as app:

    gr.Markdown("# Capivara Financeira no Reino das Moedas")

    with gr.Row():

        with gr.Column(scale=2):

            chatbot = gr.Chatbot(
                value=[{"role": "assistant", "content": mensagem_inicial}],
                type="messages",
                height=400
            )

            msg = gr.Textbox(placeholder="Pergunte algo...")

            with gr.Row():
                enviar = gr.Button("Enviar")
                limpar = gr.Button("Limpar")

            audio_output = gr.Audio(label="Áudio", autoplay=True)
            grafico_output = gr.Plot(value=capivara_placeholder())

            enviar.click(
                responder_ui,
                [msg, chatbot],
                [msg, chatbot, grafico_output, audio_output]
            )

            msg.submit(
                responder_ui,
                [msg, chatbot],
                [msg, chatbot, grafico_output, audio_output]
            )

            def limpar_chat():
                return "", [{"role": "assistant", "content": mensagem_inicial}], capivara_placeholder(), None

            limpar.click(
                limpar_chat,
                [],
                [msg, chatbot, grafico_output, audio_output]
            )

        with gr.Column(scale=1):

            gr.Markdown("## 📊 Gráficos")

            btn_atendimento = gr.Button("Atendimento")
            btn_transacoes = gr.Button("Transações")

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

if __name__ == "__main__":
    app.launch(share=True)