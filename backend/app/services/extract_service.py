import re


def extrair_dados(texto: str) -> dict:
    """
    Extrai informações básicas do texto de um currículo.

    Parâmetros:
        texto (str): Texto extraído do currículo.

    Retorno:
        dict: Informações encontradas.
    """

    # Procura um endereço de e-mail
    email = re.search(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        texto
    )

    return {
        "nome": None,
        "email": email.group(0) if email else None,
        "telefone": None,
        "linkedin": None,
        "github": None
    }