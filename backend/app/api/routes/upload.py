from fastapi import APIRouter, File, UploadFile

from app.services.upload_service import salvar_curriculo

# Cria um roteador para as rotas de upload
router = APIRouter()


@router.post("/upload")
def enviar_curriculo(arquivo: UploadFile = File(...)):
    """
    Recebe um currículo enviado pelo usuário.

    Encaminha o arquivo para o serviço responsável
    por realizar o salvamento.

    Parâmetros:
        arquivo (UploadFile): Arquivo enviado pelo usuário.

    Retorno:
        dict: Resultado do processo de upload.
    """

    return salvar_curriculo(arquivo)