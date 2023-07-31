FROM python:3.11

WORKDIR /code

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . /code/
RUN pip install pipenv
RUN pipenv install --dev
