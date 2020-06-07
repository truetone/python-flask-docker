FROM python:buster

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install -y ruby nodejs npm

RUN npm install -g sass

RUN pip install -r ./requirements.txt
