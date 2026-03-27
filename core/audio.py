# 🔊 GERAÇÃO DE ÁUDIO

import tempfile
from gtts import gTTS


def gerar_audio(texto: str):
    """Gera áudio a partir de texto usando gTTS"""

    try:
        if not texto or not texto.strip():
            return None

        # 🔒 Limite para evitar erro no gTTS
        texto_limpo = texto.strip()[:1000]

        # 🎙️ Geração do áudio
        tts = gTTS(text=texto_limpo, lang="pt-br")

        # 📁 Arquivo temporário
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        caminho = temp_file.name
        temp_file.close()  # importante no Windows

        # 💾 Salva o áudio
        tts.save(caminho)

        print(f"✅ Áudio gerado: {caminho}")

        return caminho

    except Exception as e:
        print("❌ Erro ao gerar áudio:", e)
        return None