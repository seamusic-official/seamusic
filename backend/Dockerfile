FROM python:3.11.9

COPY . /backend
WORKDIR /backend

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN poetry install

CMD ["make", "run"]