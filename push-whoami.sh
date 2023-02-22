#!/bin/sh

# If you want to push it manually

GITHUB_NAME=jennerwein
TAG=v1.2 # Update 230212
NAME=whoami

docker login
docker push ${GITHUB_NAME}/${NAME}:latest
docker tag ${GITHUB_NAME}/${NAME}:latest ${GITHUB_NAME}/${NAME}:${TAG}
docker push ${GITHUB_NAME}/${NAME}:${TAG}


