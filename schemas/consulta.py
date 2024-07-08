from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
from model.consulta import Consulta

from model import Session
from flask import redirect, request

from schemas.error import ErrorAgendaConsultaSchema, ErrorConsultaDelSchema


from flask_cors import CORS

from flask.views import View

from logger import logger

from sqlalchemy.exc import IntegrityError

class ConsultaSchema(BaseModel):
    """ Define como uma nova consulta a ser inserida é representada
    """
    id: int = 1
    data: str = "2023/12/09"
    horario: str= "10:00"
    paciente_id: int = 1


class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido é representado 
    """
    id:int = 1
    nome: str = "Phillip"
    sobrenome: str = "Sherman"
    cpf: str = "74954962072"
    data_nascimento: str = "1989-04-15"
    plano_saude: bool = True


class ListagemConsultaViewSchema(BaseModel):
    """ Define como uma consulta agendada deve ser retornada e apresentada no front-end: 
        Constam dados do paciente e da respectiva consulta na tabela.
    """
    nome: str = "Phillip"
    sobrenome: str = "Sherman"
    cpf: str = "74954962072"
    data_nascimento: str = "1989-04-15"
    data: str = "2023/12/09"
    horario: str= "10:00"
    plano_saude: bool = True
    logradouro: str = "Avenida Atlântica"
    
    
def apresenta_consultas(consultas_pacientes):
    """Faz a busca por todos as consultas agendadas

    Retorna uma representação da listagem de consultas.
    """

    result = []
    for consulta, paciente in consultas_pacientes:
        result.append({
            "nome": paciente.nome,
            "sobrenome": paciente.sobrenome,
            "cpf": paciente.cpf,
            "data_nascimento": paciente.data_nascimento,
            "data_consulta": consulta.data,
            "horario_consulta": consulta.horario,
            "plano_saude": paciente.plano_saude,
            "logradouro": paciente.logradouro,
            "numero" : paciente.numero,
            "complemento" : paciente.complemento,
            "bairro" : paciente.bairro,
            "cidade": paciente.cidade,
            "cep": paciente.cep,
        })

    return {"consultas_pacientes": result}


class AgendaConsultaSchema(BaseModel):
    """ Define como deve ser a estrutura do dado inserido na tabela do banco de dados.
    """
    mesage: str = "Consulta agendada com sucesso!"
    

class ConsultaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    mesage: str = "Consulta desmarcada com sucesso!"
    horario: str = "10:30"
    data: str = "23-10-2023"


class CPPostSchema(BaseModel):

    nome: str = "Rafael"
    sobrenome: str = "Rodrigues"
    cpf: str = "024.078.227-57"
    data_nascimento: str = "09-09-1998"
    data_consulta: str = "23-10-2023"
    horario_consulta: str = "10:30"
    plano_saude: str = "Sim"    
    logradouro: str = "Rua Araguaia"
    numero: str = "1320"
    complemento = "701"
    bairro = "Freguesia"
    cidade = "Rio de Janeiro"
    cep = "22745-271"

class EdicaoSchema(BaseModel):

    id_paciente: str = ""
    nome: str = "Casimiro"
    sobrenome: str = "Rodrigues"
    cpf: str = "024.078.227-57"
    data_nascimento: str = "09-09-1998"
    id_consulta: str = ""
    data_consulta: str = "15-11-2023"
    horario_consulta: str = "15:30"
    plano_saude: str = "Sim"    
    logradouro: str = "Rua Araguaia"
    numero: str = "1420"
    complemento = "801"
    bairro = "Taquara"
    cidade = "Rio de Janeiro"
    cep = "22745-271"