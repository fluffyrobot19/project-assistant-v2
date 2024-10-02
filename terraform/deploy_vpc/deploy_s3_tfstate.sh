#!/bin/bash
source ../../.env

aws s3api create-bucket --bucket pa-tfstate-bucket --region $AWS_REGION --create-bucket-configuration LocationConstraint=$AWS_REGION 
