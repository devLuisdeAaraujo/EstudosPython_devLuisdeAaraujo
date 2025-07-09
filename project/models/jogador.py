from pydantic import BaseModel

class jogador(BaseModel):
    jogador_name : str
    jogador_idade : int
    jogador_time :str

