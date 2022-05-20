FROM --platform=linux/amd64 tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update && apt-get install -y \
&& apt-get install -y postgresql-client \
&& pip install --no-cache-dir --upgrade pip

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt 

COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80
