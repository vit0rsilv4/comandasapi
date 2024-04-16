


from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int
    nome: str
    cpf: str
    telefone: str
