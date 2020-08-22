FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /var/www/queens
COPY requirements.txt requirements.txt
RUN apk update \
 && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -qU pip
RUN pip install -r requirements.txt