from model import Session
from model.paciente import Paciente
from model.consulta import Consulta
from typing import Optional, List

def apresenta_consultas(consultas_pacientes):
    """Faz a busca por todos as consultas agendadas

    Retorna uma representação da listagem de consultas.
    """

    result = []
    for consulta, paciente in consultas_pacientes:
        result.append({
            "id_paciente": paciente.id,
            "nome": paciente.nome,
            "sobrenome": paciente.sobrenome,
            "cpf": paciente.cpf,
            "data_nascimento": paciente.data_nascimento,
            "id_consulta": consulta.id,
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