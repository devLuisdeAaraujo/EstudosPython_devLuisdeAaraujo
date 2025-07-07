from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()
jogadores = {
    1: {
        "nome":"Fulano",
        "idade":22,
        "time":"Palmeiras"
    },
    2:{
        "nome":"Gustavo Gomez",
        "idade":29,
        "time":"Palmeiras"

    }
}

@app.get("/")
def blaal():
    return jogadores

@app.get("/get-jogador/{id_jogador}")
def get_jogar(id_jogador:int):
    return jogadores[id_jogador]
@app.get("/get-jogador-time")
def get_jogar_time(time:str):
    for i in jogadores:
        if jogadores[i]["time"] == time:
            return jogadores[i]
        return {"Dados":"Nao encontrado"}
class jogador(BaseModel):
    nom:str
    idade:int
    time:str
class atualiza_jogador(BaseModel):
    nom:str
    idade:int
    time:str
@app.post("/inserir_jogador/{id_jogador}")
def inserir_jogadores(id_jogador:int,jogador: jogador):
    if id_jogador in jogadores:
        return {"Mensagem":"Jogador ja existe"}
    jogadores[id_jogador] = jogador
    return jogadores[id_jogador]
class NoneJogaor(BaseModel):
    nom:str = None
    idade:int = None
    tiem:str = None
@app.delete("/deletear_jogadores{id_jogador}")
def delete_jogador(id_jogador:int,jogador:NoneJogaor):
    jogadores[id_jogador] = jogador
@app.put("/att_dados{id_jogador}")
def att_dados(id_jogador:int,jogador:atualiza_jogador):
    jogadore[id_jogador] = jogador    
    