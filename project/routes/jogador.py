from fastapi import APIRouter
from config.database import Conectar
from models.jogador import jogador

jogador_router =APIRouter()
conexao = Conectar()
collection = conexao.get_collection()
@jogador_router.get("/")
async def inicio():
    return "Bem vindo ao Full Stack Farm"
@jogador_router.post("/inserir_jogador/{id_jogador}")
async def inserir_jogadores(id_jogador:int,jogador:jogador):
    jogador_dict = jogador.dict()
    jogador_dict["_id"] = id_jogador
    resultado = await collection.insert_one(jogador_dict)
    return {"id_inserido":str(resultado.inserted_id)}
