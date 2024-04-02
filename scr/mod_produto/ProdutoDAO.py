from fastapi import APIRouter

router = APIRouter()

# Criar os endpoints de Cliente: GET, POST, PUT, DELETE
@router.get("/produto/", tags=["Produto"])
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/produto/{id}", tags=["Produto"])
def get_cliente(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/produto/", tags=["Produto"])
def post_cliente():
    return {"msg": "post executado"}, 200

@router.put("/produto/{id}", tags=["Produto"])
def put_cliente(id: int):
    return {"msg": "put executado"}, 201

@router.delete("/produto/{id}", tags=["Produto"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201
