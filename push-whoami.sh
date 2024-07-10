#!/bin/sh

# If you want to push it manually

# https://hub.docker.com/repository/docker/jennerwein/whoami/general
GITHUB_NAME=jennerwein
NAME=whoami
# TAG=v1.2     # Update 230212
TAG=v1.2.1   # Update 240710

docker login
docker push ${GITHUB_NAME}/${NAME}:latest
docker tag ${GITHUB_NAME}/${NAME}:latest ${GITHUB_NAME}/${NAME}:${TAG}
docker push ${GITHUB_NAME}/${NAME}:${TAG}


