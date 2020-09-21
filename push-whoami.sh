#!/bin/sh

# If you want to push it manually

GITHUB_NAME=jennerwein
TAG=200921
NAME=whoami

docker login

docker push ${GITHUB_NAME}/${NAME}:latest 
docker push ${GITHUB_NAME}/${NAME}:${TAG}


