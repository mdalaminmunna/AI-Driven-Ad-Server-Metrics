#!/bin/bash

#Build the docker image
docker build -t ad_server_metrics .

#Run the docker image
docker-compose up -d

echo "Ad Server Metrics Application Deployed!"