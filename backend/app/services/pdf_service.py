import fitz


def ler_pdf(caminho_pdf):
    """
    Lê um arquivo PDF e retorna todo o texto encontrado.

    Parâmetros:
        caminho_pdf (str): Caminho do arquivo PDF.

    Retorno:
        str: Texto extraído do PDF.
    """

    texto = ""

    # Abre o arquivo PDF
    with fitz.open(caminho_pdf) as pdf:

        # Percorre todas as páginas
        for pagina in pdf:

            # Junta o texto de cada página
            texto += pagina.get_text()

    return texto