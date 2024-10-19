#!/bin/bash

os=$(uname)
echo "Welcome to running Project Assistant!"
echo "Your os has been identified as "$os"".

prompt() {
	echo "You can run PA locally, in Docker or in AWS with the help of Terraform. Please enter the number of your choice while taking the dependencies into consideration:"
	echo "	1. run locally - dependencies: python3, postgresql"
	echo "	2. run in Docker - dependencies: docker, docker-compose"
	echo "	3. run in AWS with Terraform - dependencies: AWS authentication, terraform"

	while true; do
		read user_choice

		if [[ "$user_choice" == "1" ]]; then
			cd scripts
			./process_checks.sh "$1" "local"
			./run_local.sh
			break
		elif [[ "$user_choice" == "2" ]]; then
			cd scripts
			./process_checks.sh "$1" "docker"
			./run_docker.sh
			break
		elif [[ "$user_choice" == "3" ]]; then
			echo "$user_choice"
			break
		else
			echo "Invalid input. Please choose from the above options."
		fi
	done
}

while true; do
	read -p "Please confirm with 'y' otherwise press 'q' to exit the program: " confirmation

	if [[ "$confirmation" == "y" ]]; then
		prompt "$os"
		break
	elif [[ "$confirmation" == "q" ]]; then
		exit 0
	else
		echo "Invalid input."
	fi
done
