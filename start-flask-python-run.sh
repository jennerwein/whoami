#!/bin/sh

TAG=v1
NAME=flask-python-run

# Aufräumen
docker container stop ${NAME}
docker container rm ${NAME}

# Zuerst das Image bauen
docker rmi jennerwein/${NAME}:${TAG}
docker build -t jennerwein/${NAME}:${TAG} .

# Starten des Images
docker run -p 8002:8080 --name ${NAME} --restart=always -d jennerwein/${NAME}:${TAG}

