#!/bin/sh

TAG=200707
NAME=whoami-py

docker login

docker push jennerwein/${NAME}:latest 
docker push jennerwein/${NAME}:${TAG}


