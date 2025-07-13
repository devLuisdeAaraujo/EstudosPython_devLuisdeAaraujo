from fastapi import APIRouter,HTTPException
from config.database import Conectar
from models.jogador import jogador
from schemas.jogador import *
from pymongo.errors import *
from bson import ObjectId




jogador_router =APIRouter()
conexao = Conectar()
collection = conexao.get_collection()
@jogador_router.get("/")
async def inicio():
    return "Bem vindo ao Full Stack Farm"
@jogador_router.get("/jogadores")
async def lista_jogadores():
    resultado = collection.find()
    return listaJogadoresEntidade(resultado)
@jogador_router.get("/jogadores/{_id_jogador}")
async def buscar_jogadores_pelo_id(id_jogador:int):
    buscar = collection.find_one({"_id":id_jogador})
    if not buscar:
        return{"mensagem":"Jogador Nao cadastrado"}
    return listaJogadoresEntidade(collection.find(buscar))
@jogador_router.post("/inserir_jogador/{id_jogador}")
async def inserir_jogadores(id_jogador:int,jogador:jogador):
    jogador_dict = jogador.dict()
    jogador_dict["_id"] = id_jogador
    try:
        resultado = collection.insert_one(jogador_dict)
        return listaJogadoresEntidade(collection.find())
    except DuplicateKeyError:
        raise HTTPException(status_code=400,detail="Document with this ID already exists.")
@jogador_router.put("/atualizacaojogadores{id_jogador}")
async def atualizando_jogador(id_jogador:int,jogador:jogador):
    atualizar= collection.find_one_and_update(
        {
            "_id":id_jogador
        },{
            "$set":jogador.dict()
        }
    )
    if not atualizar:
        raise HTTPException(status_code=422, detail="Jogador não encontrado para atualização.")
    
    return listaJogadoresEntidade(([collection.find_one(atualizar)]))

@jogador_router.delete("/jogadores/{id_jogador}/limpar_campos")
async def limpar_campos_do_jogador(id_jogador: int):
    jogador_removido = collection.find_one_and_delete({"_id": id_jogador})


    if not jogador_removido:
        raise HTTPException(status_code=404, detail="Jogador não encontrado.")

    return {"mensagem": "Jogador deletado com sucesso."}
    
