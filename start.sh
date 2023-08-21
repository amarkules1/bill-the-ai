#!/bin/bash
app="bill-the-ai"
docker build -t ${app} .
docker run -d -p 80:80 \
  --name=${app} \
  -v $PWD:/app ${app}
read -n1 -s