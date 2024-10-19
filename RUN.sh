#!/bin/bash

os=$(uname)
echo "Welcome to running Project Assistant!"
echo "Your os has been identified as "$os"".

while true; do
	read -p "Please confirm with 'y' otherwise press 'q' to exit the program: " confirmation

	if [[ "$confirmation" == "y" ]]; then
		printf "\nYou can run PA locally, in Docker or in AWS with the help of Terraform. Please enter the number of your choice while taking the dependencies into consideration:\n"
		echo "	1. run locally - dependencies: python3, postgresql"
		echo "	2. run in Docker - dependencies: docker, docker-compose"
		echo "	3. run in AWS with Terraform - dependencies: AWS authentication, terraform"

		while true; do
			read user_choice

			if [[ "$user_choice" == "1" ]]; then
				cd scripts
				process_output=$(./process_checks.sh "$os" "local")
				echo "$process_output"
				if echo "$process_output" | grep -q '✗'; then
					echo "An error has occured. Exiting the program now."
					exit 1
				fi
				./run_local.sh
				break
			elif [[ "$user_choice" == "2" ]]; then
				cd scripts
				process_output=$(./process_checks.sh "$os" "docker") 
				echo "$process_output"
				if echo "$process_output" | grep -q '✗'; then
					echo "An error has occured. Exiting the program now."
					exit 1
				fi
				./run_docker.sh
				break
			elif [[ "$user_choice" == "3" ]]; then
				echo "$user_choice"
				break
			else
				echo "Invalid input. Please choose from the above options."
			fi
		done
		break
	elif [[ "$confirmation" == "q" ]]; then
		exit 0
	else
		echo "Invalid input."
	fi
done
