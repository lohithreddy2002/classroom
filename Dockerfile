FROM python:3.9-slim
WORKDIR /app
ADD . ./app
COPY ./requirements.txt /app/requirements.txt
RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app/classroom

