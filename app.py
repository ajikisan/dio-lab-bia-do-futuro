# 🌐 app.py — Interface Gradio

import gradio as gr
from main import responder
from ui.graficos import (
    grafico_atendimento_com_historia,
    grafico_transacoes_com_historia,
    capivara_placeholder
)

# 🏰 Mensagem inicial
mensagem_inicial = """
🏰 Bem-vindo ao Reino das Moedas!
Eu sou a Capivara Financeira, guardiã divertida que transforma o dinheiro em aventuras mágicas.
💰 Seu tesouro cresce nos rios das entradas, enfrenta dragões das saídas e segue protegido pelas muralhas rumo às conquistas épicas.
Sempre ao seu lado, sem substituir o valor das conversas humanas.
"""

# =============================
# 🚀 Funções de interface (UI)
# =============================
def responder_ui(pergunta, historico_chat):
    resposta, historico_chat, grafico, audio = responder(pergunta, historico_chat)
    return "", historico_chat, grafico, audio  # primeiro valor sempre vazio → limpa input


def limpar_ui():
    return "", [], capivara_placeholder(), None


# =============================
# 🎨 Tema
# =============================
custom_theme = gr.themes.Soft(
    primary_hue="violet",
    secondary_hue="purple",
    neutral_hue="gray"
).set(
    body_background_fill="linear-gradient(135deg, #f5f3ff, #ede9fe)",
    button_primary_background_fill="linear-gradient(90deg, #7c3aed, #9333ea)",
    button_primary_background_fill_hover="linear-gradient(90deg, #6d28d9, #7c3aed)",
    button_secondary_background_fill="linear-gradient(90deg, #a78bfa, #c4b5fd)"    
)


# =============================
# 🧱 Interface
# =============================
with gr.Blocks(theme=custom_theme) as demo:   # ✅ tema volta aqui
    gr.Markdown(mensagem_inicial)

    chatbot = gr.Chatbot(
        label="Capivara Financeira no Reino das Moedas",
        type="messages",          # ✅ formato novo
        allow_tags=False          # ✅ evita warning futuro
    )

    entrada = gr.Textbox(
        label="Pergunte sobre suas moedas",
        placeholder="Digite aqui..."
    )

    with gr.Row():
        enviar_btn = gr.Button("🪄 Enviar")
        limpar_btn = gr.Button("🧹 Limpar conversa")
        grafico_trans_btn = gr.Button("📊 Ver gráfico de transações")
        grafico_atend_btn = gr.Button("📞 Ver gráfico de atendimentos")

    grafico_out = gr.Image(label="Visualização")
    audio_out = gr.Audio(label="Resposta em áudio", type="filepath")

    # =============================
    # 🔁 Fluxo principal
    # =============================
    def fluxo(pergunta, chat_hist):
        return responder_ui(pergunta, chat_hist)

    entrada.submit(
        fluxo,
        inputs=[entrada, chatbot],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )

    enviar_btn.click(
        fluxo,
        inputs=[entrada, chatbot],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )

    limpar_btn.click(
        limpar_ui,
        inputs=[],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )

    grafico_trans_btn.click(
        grafico_transacoes_com_historia,
        inputs=[None],   # ✅ aceita argumento opcional
        outputs=[grafico_out, chatbot, audio_out, entrada]
    )

    grafico_atend_btn.click(
        grafico_atendimento_com_historia,
        inputs=[None],   # ✅ aceita argumento opcional
        outputs=[grafico_out, chatbot, audio_out, entrada]
    )


# =============================
# 🚀 Inicialização
# =============================
if __name__ == "__main__":
    demo.launch(share=True)
