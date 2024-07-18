FROM python:slim

WORKDIR /app

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements/dev.txt

RUN pip install -r requirements/dev.txt

COPY . .