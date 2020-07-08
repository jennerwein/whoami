#!/bin/sh

# If you want to push it manually

TAG=200708
NAME=whoami

docker login

docker push jennerwein/${NAME}:latest 
docker push jennerwein/${NAME}:${TAG}


