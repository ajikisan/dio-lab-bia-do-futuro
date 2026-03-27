# 🔤 Funções de normalização de texto

from unidecode import unidecode


def normalizar(s: str) -> str:
    """
    Normaliza texto para facilitar comparação:
    - lowercase
    - remove acentos
    - remove espaços extras
    """
    try:
        if not isinstance(s, str):
            return ""

        return unidecode(s.lower().strip())

    except Exception:
        return ""