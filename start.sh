#!/bin/bash
app="bill-the-ai"
docker stop ${app}
docker rm ${app}
docker rmi ${app}
docker build -t ${app} .
docker run -d -p 443:443 \
  --name=${app} \
  -v $PWD:/app ${app}
read -n1 -s