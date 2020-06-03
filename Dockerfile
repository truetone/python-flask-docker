FROM python:buster

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN pip install -r ./requirements.txt
