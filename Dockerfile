# Base Image
FROM python:3.6-alpine as BASE

RUN apk add --no-cache linux-headers g++ postgresql-dev gcc build-base linux-headers ca-certificates python3-dev libffi-dev libressl-dev pcre-dev libpq libxslt-dev
RUN pip wheel --wheel-dir=/root/wheels psycopg2
RUN pip wheel --wheel-dir=/root/wheels cryptography

# Actual Image

FROM python:3.6-alpine as RELEASE

EXPOSE 8080
WORKDIR /app

RUN apk add --no-cache 
RUN apk add postgresql-dev gcc python3-dev build-base linux-headers pcre-dev
RUN pip install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip
RUN apk add py3-gevent uwsgi uwsgi-python3 uwsgi-http uwsgi-gevent3
ENV POSTGRES_USER="amit" POSTGRES_PASSWORD=7045098760 POSTGRES_HOST=database POSTGRES_PORT=5432 POSTGRES_DB="postgres"

COPY . /app

COPY --from=BASE /root/wheels /root/wheels

ENV UWSGI_PROFILE=core
COPY requirements.txt .
RUN pip install -r requirements.txt

    
CMD ["uwsgi", "--socket", "0.0.0.0:8000", "--module", "customer_app.wsgi"]
