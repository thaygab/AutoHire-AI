from fastapi import FastAPI

from app.api.router import router

# Cria a aplicação FastAPI
app = FastAPI()

# Registra todas as rotas da aplicação
app.include_router(router)