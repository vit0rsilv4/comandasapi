from pydantic import BaseModel

class Cliente(BaseModel):
    id_Cliente: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    grupo: int
    senha: str = None
#Vitor Manoel