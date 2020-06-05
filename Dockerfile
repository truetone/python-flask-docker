FROM python:buster

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . .

RUN apt update && apt install -y ruby

RUN gem install bourbon

RUN pip install -r ./requirements.txt
