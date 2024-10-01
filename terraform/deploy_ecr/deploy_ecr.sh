#!/bin/bash
source ../../.env

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com
# cd ..
# docker-compose build flask_app
# docker tag flask_app:latest 891377360878.dkr.ecr.eu-west-1.amazonaws.com/flask_app:latest
# docker push <account-id>.dkr.ecr.us-west-1.amazonaws.com/my-app-repo:latest



