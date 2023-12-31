# MAISTODOS API

## Pré-requisitos

A aplicação web e o banco de dados rodam em containers do docker.

Instalar o docker: https://docs.docker.com/get-docker/


## Rodando migração

Depois de baixar a aplicação pela primeira vez ou atualizar o repositório local
ceritfique-se de rodar a migração do banco de dados

```shell
docker compose run --rm web pipenv run ./manage.py migrate
```

## Rodando Aplicação
```shell
docker compose up
```
Aqui você deve ter banco de dados na porta 5432 e o servidor web rodando e respondendo as requisições na porta 8000.
Cerifique-se de que não há nenhuma outra aplicação na sua maquina utilizando essas duas portas.

## Rodando testes automatizados
```shell
docker compose run --rm web pipenv run ./manage.py test
```

## Testando manualmente a aplicação

Você precisa se autenticar com usuário padrão do Django
```shell
# abra o terminal do Django dentro do container
docker compose run --rm web pipenv run ./manage.py shell
```
Agora você deve estar dentro de um shell do Django dentro do container
```python 
# criando usuario qualquer para teste
from django.contrib.auth.models import User
User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
```
Ao relaizar uma chamada HTTP no endpoint de autenticação você deverá receber um par de tokens
```http request
POST http://localhost:8000/api/token/
Content-Type: application/json

{
    "username": "john",
    "password": "johnpassword"
}
```
Formato de Resposta
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MDkxMTI0MywiaWF0IjoxNjkwODI0ODQzLCJqdGkiOiI3ZDU2NDc0YmExMTk0NTQwYjQ1OGExZjRjYjBkODlmMiIsInVzZXJfaWQiOjN9.43sG5rUzkYEi4T5F_oM-mFCn194Rk1bGsh5eYyZpUVM",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwODI1MTQzLCJpYXQiOjE2OTA4MjQ4NDMsImp0aSI6IjVhNTZmNWM5ZWM0NDQ4NDNiNDc4ZDA5NjA0Y2FmY2EyIiwidXNlcl9pZCI6M30.Bh1ACfZd82m8G8Smps3PxoKcckiLPzhgU7dHLd3rnDE"
}
```
Basta utilizar o access token nas demais requisições
```http request
GET http://localhost:8000/api/v1/credit-card/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwODI1MTQzLCJpYXQiOjE2OTA4MjQ4NDMsImp0aSI6IjVhNTZmNWM5ZWM0NDQ4NDNiNDc4ZDA5NjA0Y2FmY2EyIiwidXNlcl9pZCI6M30.Bh1ACfZd82m8G8Smps3PxoKcckiLPzhgU7dHLd3rnDE
```

## Deploy e ambiente de producao

Para realizar o deploy ou conectar o container do banco de dados de producao
basta fazer uma copia do seguinte arquivo:
```shell
cp .env.example .env
# edite o .env inserindo os dados do banco de producao
```

Aqui você pode usar os mesmos comandos utilizados no teste local para criar um usuário
no banco de dados de produção.
O docker vai carregar automaticamente as variaveis de ambiente definidas em um arquivo `.env`

Para o deploy você precisa instalar o Node.js: https://nodejs.org/en

```shell
# instalando as dependencias 
npm install
./node_modules/serverless/bin/serverless.js deploy
```

## Code Formatter
Antes de commitar, rodar os formatadores de código
```shell
docker compose run --rm web pipenv run black .
docker compose run --rm web pipenv run isort .
```

## Considerações sobre o projeto
Foi utilizado o [Pipenv](https://pipenv.pypa.io/en/latest/) para simplificar o gerenciamento de dependencias

Inicialmente não seria utilizado o Docker, porém ficou mais fácil de garantir que o projeto poderia rodar em diferentes
sistemas operacionais sem a necessidade de instalar e gerenciar manualemente a versão do Python.

### Dependencias
* [`django`](https://docs.djangoproject.com/en/4.2/): pode parecer um pouco de "overengeniering" usar um framework tão completo e robusto para uma API simples, com apenas um recurso. Porém é compensando na simplicidade do código, devido ao conjunto de funcionalidades e "baterias incluidas", como por exemplo itegração com banco de dados e ambiente de testes de integração;
* [`python-creditcard`](https://github.com/MaisTodos/python-creditcard): validação do número de cartão de crédito.
* [`django-cryptography`](https://github.com/georgemarshall/django-cryptography): para gravar número do cartão de crédito de forma criptografada.
* [`djangorestframework`](https://www.django-rest-framework.org): recursos para simplificar a construção da API.
* [`psycopg`](https://www.psycopg.org): driver para o PostgreSQL.
* [`djangorestframework-simplejwt`](https://github.com/jazzband/djangorestframework-simplejwt): simplificar o uso de tokens JWT para autenticação.

Ambiente de desenvolvimento:
* [`black`](https://github.com/psf/black): formatador de código padronizado.
* [`isort`](https://github.com/pycqa/isort/): organizar imports de forma padronizada.
* [`freezegun`](https://github.com/spulec/freezegun): mock para testes automatizados envolvendo data e horário.
