#!/bin/bash
source ../../.env

public_ip=$(jq .pa_ec2_public_ip.value ./pa_ec2_public_ip.json | sed 's/^"\(.*\)"$/\1/')

ssh -i $AWS_KEY_PATH ec2-user@$public_ip
