#!/bin/sh

GITHUB_NAME=jennerwein
TAG=v1.1
NAME=whoami

# Clean up
docker container stop ${NAME}
docker container rm ${NAME}

# First, build the image
docker rmi ${GITHUB_NAME}/${NAME}:${TAG}
docker rmi ${GITHUB_NAME}/${NAME}:latest
docker build -t ${GITHUB_NAME}/${NAME}:latest -t ${GITHUB_NAME}/${NAME}:${TAG} .

# Start the image
docker run -p 8080:8080 --name ${NAME} --restart=always -d ${GITHUB_NAME}/${NAME}:${TAG}

