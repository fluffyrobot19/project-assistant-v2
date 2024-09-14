#!/bin/bash

echo "Welcome to running Project Assistant!"

# checking all processes
./process_checks.sh

if ./process_checks.sh | grep -q '✗'; then
	exit 0
fi

# running docker
read -p "The Dockerfile and docker-compose.yml files will be run now. Please press 'y' in order to proceed: " user_input
echo

if [[ "$user_input" == "y" ]]; then
	docker-compose build
	docker-compose up -d
	echo
	echo "Visit Project Assistant at http://localhost:3000"
	read -p "Press 'd' in order to stop the program and remove the Docker image: " down
	if [[ "$down" == "d" ]]; then
		docker-compose down
		docker rmi $(docker images | awk '{print $1}' | awk 'NR==2')
	fi
else
	echo "Exiting the program now."
	exit 0
fi

