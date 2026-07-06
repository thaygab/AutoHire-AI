from fastapi import APIRouter

from app.api.routes.home import router as home_router

# Roteador principal da aplicação
router = APIRouter()

# Registra as rotas da página inicial
router.include_router(home_router)