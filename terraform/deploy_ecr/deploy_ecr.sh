#!/bin/bash
source ../../.env

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com
cd ../..
docker-compose build web
docker tag project-assistant-web:latest $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/project-assistant-ecr:latest
cd terraform/deploy_ecr
terraform plan
terraform apply -auto-approve
docker push $AWS_ID.dkr.ecr.$AWS_REGION.amazonaws.com/project-assistant-ecr:latest



