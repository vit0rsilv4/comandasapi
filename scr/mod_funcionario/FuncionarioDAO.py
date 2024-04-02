from fastapi import APIRouter

router = APIRouter()

# import da persistência
import db
from mod_funcionario.FuncionarioModel import FuncionarioDB
from mod_funcionario.Funcionario import Funcionario


###
@router.get("/funcionario/{id}", tags=["Funcionário"])
def get_funcionario(id: int):
    try:
        session = db.Session()
        # busca um com filtro
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).all()
        session.close()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400

#####
@router.post("/funcionario/", tags=["Funcionário"])
def post_funcionario(corpo: Funcionario):
    try:
        session = db.Session()
        dados = FuncionarioDB(
            None, corpo.nome, corpo.matricula, corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha
        )

        session.add(dados)
        session.commit()
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

##router put
@router.put("/funcionario/{id}", tags=["Funcionário"])
def put_funcionario(id: int, corpo: Funcionario):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one()
        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo
        session.add(dados)
        session.commit()
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

### router delete
@router.delete("/funcionario/{id}", tags=["Funcionário"])
def delete_funcionario(id: int):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario == id).one()
        session.delete(dados)
        session.commit()
        return {"id": dados.id_funcionario}, 200
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

### router post
# valida o cpf e senha informado pelo usuário
@router.post("/funcionario/login/", tags=["Funcionário - Login"])
def login_funcionario(corpo: Funcionario):
    try:
        session = db.Session()
        # one(), requer que haja apenas um resultado no conjunto de resultados
        # é um erro se o banco de dados retornar 0, 2 ou mais resultados e uma exceção será gerada
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == corpo.cpf).filter(FuncionarioDB.senha == corpo.senha).one()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

##router get
# valida o cpf e senha informado pelo usuário
@router.post("/funcionario/login/", tags=["Funcionário - Login"])
def login_funcionario(corpo: Funcionario):
    try:
        session = db.Session()
        # one(), requer que haja apenas um resultado no conjunto de resultados
        # é um erro se o banco de dados retornar 0, 2 ou mais resultados e uma exceção será gerada
        dados = session.query(FuncionarioDB).filter(FuncionarioDB.cpf == corpo.cpf).filter(FuncionarioDB.senha == corpo.senha).one()
        return dados, 200
    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()
