from fastapi import FastAPI

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