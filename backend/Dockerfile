FROM python:latest

WORKDIR /app

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFED 1

COPY requirements/dev.txt requirements/dev.txt

RUN pip install -r requirements/dev.txt

COPY . .