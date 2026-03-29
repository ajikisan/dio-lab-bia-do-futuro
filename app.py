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
    # Retorna textbox vazio para limpar input, manter histórico e mostrar gráfico/áudio
    return "", historico_chat, grafico, audio

def limpar_ui():
    # Reset do histórico, input, gráficos e áudio
    return "", [], capivara_placeholder(), None

# =============================
# 🎨 Tema personalizado Gradio
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
# 🏗️ Interface Gradio
# =============================
with gr.Blocks(theme=custom_theme) as demo:
    gr.Markdown(mensagem_inicial)

    # Chat e entrada de texto
    chatbot = gr.Chatbot(
        label="Capivara Financeira no Reino das Moedas",
        type="messages",
        allow_tags=False
    )
    entrada = gr.Textbox(
        label="Pergunte sobre suas moedas",
        placeholder="Digite aqui..."
    )

    # Botões de controle
    with gr.Row():
        enviar_btn = gr.Button("🚀 Enviar")
        limpar_btn = gr.Button("🧹 Limpar")
        
        
        grafico_trans_full_btn = gr.Button("📊 Gráfico de Transações")
        grafico_atend_full_btn = gr.Button("📞 Gráfico de Atendimentos")

    # Saídas
        grafico_out = gr.Image(
        label="Visualização",
        value=capivara_placeholder()  # <-- Capivara já aparece ao iniciar
    )
    audio_out = gr.Audio(label="Resposta em áudio", type="filepath")    
      

    # =============================
    # 🔄 Função principal do fluxo
    # =============================
    def fluxo(pergunta, chat_hist):
        return responder_ui(pergunta, chat_hist)

    # Dispara ao apertar Enter
    entrada.submit(
        fluxo,
        inputs=[entrada, chatbot],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )

    # Dispara ao clicar botão enviar
    enviar_btn.click(
        fluxo,
        inputs=[entrada, chatbot],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )

    # Limpar conversa
    limpar_btn.click(
        limpar_ui,
        inputs=[],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )
    
    # =============================
    # 📊 Botões completos (gráfico + chat + áudio)
    # =============================
    grafico_trans_full_btn.click(
        fn=lambda: responder("gráfico transações", [], False),
        inputs=[],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )
    grafico_atend_full_btn.click(
        fn=lambda: responder("atendimento", [], False),
        inputs=[],
        outputs=[entrada, chatbot, grafico_out, audio_out]
    )

# =============================
# 🚀 Inicialização
# =============================
if __name__ == "__main__":
    demo.launch(share=True)