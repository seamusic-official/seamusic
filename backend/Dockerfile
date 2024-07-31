FROM python:slim

WORKDIR /backend

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/dev.txt requirements/dev.txt
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
RUN alembic upgrade head

CMD ["python", "-m", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
