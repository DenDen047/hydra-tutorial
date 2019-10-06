#!/bin/bash

NAME="main"

# env params
export MI_DATA_PATH=$1

# build & run
cd docker && \
docker-compose up --build

# clean up a container
docker rm docker_${NAME}_1
