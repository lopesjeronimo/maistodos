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
GET http://localhost:8000/api/credit-card
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwODI1MTQzLCJpYXQiOjE2OTA4MjQ4NDMsImp0aSI6IjVhNTZmNWM5ZWM0NDQ4NDNiNDc4ZDA5NjA0Y2FmY2EyIiwidXNlcl9pZCI6M30.Bh1ACfZd82m8G8Smps3PxoKcckiLPzhgU7dHLd3rnDE
```


## Antes de commitar, rodar os formatadores de código
```shell
black .
isort .
```
