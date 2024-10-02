#!/bin/bash
source ../../.env

aws s3 rm s3://pa-tfstate-bucket --recursive
aws s3api delete-bucket --bucket pa-tfstate-bucket --region $AWS_REGION 
