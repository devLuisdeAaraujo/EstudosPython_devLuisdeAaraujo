from fastapi import FastAPI
from routes.jogador import jogador_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
cliente_app = [
    "http://localhost:3000"
]
app.include_router(jogador_router)
app.middleware(
    CORSMiddleware,
    allow_origins = cliente_app,
    allow_credential =True,
    allow_methods =["*"],
    allow_headers = ["*"]
)