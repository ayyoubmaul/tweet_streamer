#!/bin/bash

while getopts "k:s:a:c:p:" opt
do
   case "${opt}" in
      k) cons_key=$OPTARG;;
      s) cons_secret=$OPTARG;;
      a) acc_token=$OPTARG;;
      c) acc_secret=$OPTARG;;
      p) pubsub_sa=$OPTARG;;
   esac
done

echo "CONSUMER_KEY=$cons_key" > .env
echo "CONSUMER_SECRET=$cons_secret" >> .env
echo "ACCESS_TOKEN=$acc_token" >> .env
echo "ACCESS_SECRET=$acc_secret" >> .env
echo 'PUBSUB_CREDS="/code/pubsub_sa.json"' >> .env

jq '.' $pubsub_sa > pubsub_sa.json

docker-compose up --build --force-recreate

> .env
echo '{}' > pubsub_sa.json
