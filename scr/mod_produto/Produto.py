from pydantic import BaseModel

class Produto(BaseModel):
    id_Produto: int = None
    nome_produto: str
    matricula: str
    fabricacao: str
    validade: str = None
    grupo: int