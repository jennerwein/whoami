#!/bin/sh

TAG=200707
NAME=whoami-py

# Aufräumen
docker container stop ${NAME}
docker container rm ${NAME}

# Zuerst das Image bauen
docker rmi jennerwein/${NAME}:${TAG}
docker rmi jennerwein/${NAME}:latest
docker build -t jennerwein/${NAME}:latest -t jennerwein/${NAME}:${TAG} .

# Starten des Images
docker run -p 8002:8080 --name ${NAME} --restart=always -d jennerwein/${NAME}:${TAG}

