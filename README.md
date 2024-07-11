# Sistema de Agendamento e Gerenciamento de Consultas (SAGC) - API

O **Sistema de Agendamento e Gerenciamento de Consultas (SAGC)** busca prover aos profissionais de secretariado 
um modo ágil e prático de agendar e administrar consultas virtualmente.

No presente projeto, o SAGC é empregado no contexto de um consultório odontológico, cujos serviços são 
prestados por um único profissional dentista. Cabe ao seu (sua) secretário(a) o uso dessa ferramenta 
para cadastrar os pacientes e marcar suas consultas.

Este projeto foi desenvolvido para o MVP da Sprint 4 da **Pós Gradução de Engenharia de Softwarer da PUC-Rio e
trata-se de uma atualização do projeto da Srint 1 do mesmo curso.**
<br>
---
<br>
## Execução da aplicação

Para executar esta aplicação, siga os passos enumerados a seguir:


### 1 - Clone o repositório

Clone o repositório através do comando abaixo:

```
[git clone (...)](https://github.com/rafarasant/PUC_MVP_SPRINT_4_BACKEND.git)
```

### 2 - Crie e execute a imagem do Docker e o container para o componente back-end da aplicação

Para que seja possível executar a aplicação, é preciso proceder primeiramente à criação tanto da imagem do Docker quanto
do container para o componente back-end da aplicação. Isso deve ser feito no diretório raiz do projeto, a partir do terminal, através do seguinte comando:

```
docker build -t flask-app .
```

Em seguida, a imagem deve ser executada através do comando abaixo:

```
docker run -d -p 5000:5000 flask-app
```

### 3 - Banco de dados

A pasta *database*, localizada na raiz do projeto, contém o arquivo *pacientes.sqlite3*. Nela já se encontram criadas as duas tabelas necessárias para a execução
da API (*paciente* e *consulta*).

### 4 - Documentação da API no navegador (Swagger)

No navegador, abra o link abaixo para visualizar o status da API em execução.

```
localhost:5000/
```

### 5 - Vídeo de apresentação da aplicação

O vídeo de apresentação do trabalho pode ser acessado através do link abaixo:

```
https://drive.google.com/file/d/1jMUT1OJBV_OoOJ0radaH3sA5VcgCTCC5/view?usp=sharing
```

### 7 - Diagrama da aplicação

O diagrama explicativo da aplicação pode ser acessado através do link abaixo:

```
https://drive.google.com/file/d/1p7vrFVLHh67FFoNMlFysfsfsFu9qZtmb/view?usp=sharing
```
