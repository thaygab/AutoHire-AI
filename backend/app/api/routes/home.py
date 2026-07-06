from fastapi import APIRouter

# Cria um roteador para as rotas da página inicial
router = APIRouter()


# Rota inicial da API
@router.get("/")
def home():
    """
    Retorna uma mensagem informando que a API está funcionando.
    """
    return {
        "message": "Bem-vindo ao AutoHire AI!"
    }