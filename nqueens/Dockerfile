FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /var/www/nqueens
COPY requirements.txt requirements.txt
RUN apk update \
 && apk add postgresql-dev gcc musl-dev
RUN pip install -r requirements.txt