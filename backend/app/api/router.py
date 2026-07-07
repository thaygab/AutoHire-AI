from fastapi import APIRouter

from app.api.routes.home import router as home_router
from app.api.routes.upload import router as upload_router

# Roteador principal da aplicação
router = APIRouter()

# Registra as rotas da página inicial
router.include_router(home_router)
router.include_router(upload_router)