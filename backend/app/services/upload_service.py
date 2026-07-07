from pathlib import Path
import shutil


# Caminho da pasta onde os currículos serão armazenados
PASTA_UPLOADS = Path("uploads")


def salvar_curriculo(arquivo):
    """
    Salva um currículo na pasta de uploads.

    Parâmetros:
        arquivo (UploadFile): Arquivo enviado pelo usuário.

    Retorno:
        dict: Mensagem indicando o resultado do salvamento.
    """

    # Garante que a pasta de uploads exista
    PASTA_UPLOADS.mkdir(exist_ok=True)

    # Define o caminho completo do arquivo
    caminho_arquivo = PASTA_UPLOADS / arquivo.filename

    # Salva o arquivo no computador
    with open(caminho_arquivo, "wb") as buffer:
        shutil.copyfileobj(arquivo.file, buffer)

    return {
        "mensagem": "Currículo salvo com sucesso!",
        "arquivo": arquivo.filename
    }