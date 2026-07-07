from fastapi import APIRouter

from app.services.upload_service import verificar_upload

# Cria um roteador para as rotas de upload
router = APIRouter()


# Rota de teste do módulo de upload
@router.get("/upload")
def upload():
    """
    Verifica se o serviço de upload está funcionando.
    """
    return verificar_upload()