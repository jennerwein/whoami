#!/bin/sh

# If you want to push it manually

GITHUB_NAME=jennerwein
TAG=v1.1
NAME=whoami

docker login

docker push ${GITHUB_NAME}/${NAME}:latest 
docker push ${GITHUB_NAME}/${NAME}:${TAG}


