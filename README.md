# MAISTODOS API

## Pré-requisitos

A aplicação web e o banco de dados rodam em containers do docker.

Instalar o docker: https://docs.docker.com/get-docker/

## Rodando Aplicação
```shell
docker compose up
```

## Rodando migração
```shell
docker compose run --rm web pipenv run ./manage.py migrate
```

## Rodando Testes
```shell
docker compose run --rm web pipenv run ./manage.py test
```
