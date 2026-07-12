import re
from app.services.knowledge_service import carregar_tecnologias

def extrair_email(texto: str) -> str | None:
    """
    Extrai o endereço de e-mail do currículo.

    Parâmetros:
        texto (str): Texto do currículo.

    Retorno:
        str | None: E-mail encontrado ou None.
    """

    email = re.search(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        texto
    )

    return email.group(0) if email else None

def extrair_telefone(texto: str) -> str | None:
    """
    Extrai o telefone do currículo.

    Parâmetros:
        texto (str): Texto do currículo.

    Retorno:
        str | None: Telefone encontrado ou None.
    """

    telefone = re.search(
        r"\(?\d{2}\)?\s?\d{4,5}-?\d{4}",
        texto
    )

    return telefone.group(0) if telefone else None

def extrair_linkedin(texto: str) -> str | None:
    """
    Extrai o link do LinkedIn do currículo.

    Parâmetros:
        texto (str): Texto do currículo.

    Retorno:
        str | None: Link do LinkedIn encontrado ou None.
    """

    linkedin = re.search(
        r"linkedin\.com/in/[\w-]+",
        texto
    )

    return linkedin.group(0) if linkedin else None

def extrair_github(texto: str) -> str | None:
    """
    Extrai o link do GitHub do currículo.

    Parâmetros:
        texto (str): Texto do currículo.

    Retorno:
        str | None: Link do GitHub encontrado ou None.
    """

    github = re.search(
        r"github\.com/[\w-]+",
        texto
    )

    return github.group(0) if github else None

def calcular_pontuacao_nome(linha: str) -> int:
    pontuacao = 0

    if len(linha.split()) >= 2:
        pontuacao += 2

    if any(caractere.isdigit() for caractere in linha):
        pontuacao -= 5

    linha_minuscula = linha.lower()

    if (
        "@" in linha_minuscula
        or "linkedin" in linha_minuscula
        or "github" in linha_minuscula
    ):
        pontuacao -= 5

    return pontuacao

def extrair_nome(texto: str) -> str | None:
    """
    Extrai o nome do candidato utilizando heurística.

    Parâmetros:
        texto (str): Texto extraído do currículo.

    Retorno:
        str | None: Nome encontrado ou None.
    """

    linhas = texto.splitlines()

    linhas = [
        linha.strip()
        for linha in linhas
        if linha.strip()
    ]

    melhor_nome = None
    maior_pontuacao = -999

    for linha in linhas[:5]:
        pontuacao = calcular_pontuacao_nome(linha)

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_nome = linha

    return melhor_nome

def extrair_habilidades(texto: str) -> list:
    """
    Extrai as tecnologias encontradas no currículo.

    Parâmetros:
        texto (str): Texto extraído do currículo.

    Retorno:
        list: Lista de tecnologias encontradas.
    """
    tecnologias = carregar_tecnologias()

    texto_minusculo = texto.lower()

    habilidades = []

    for tecnologia in tecnologias:

        padrao = rf"\b{re.escape(tecnologia)}\b"

        if re.search(
            padrao,
            texto,
            re.IGNORECASE
        ):

            habilidades.append(tecnologia)

    return habilidades

def extrair_dados(texto: str) -> dict:
    """
    Extrai informações básicas do currículo.
    """

    return {
        "nome": extrair_nome(texto),
        "email": extrair_email(texto),
        "telefone": extrair_telefone(texto),
        "linkedin": extrair_linkedin(texto),
        "github": extrair_github(texto),
        "habilidades": extrair_habilidades(texto)
    }