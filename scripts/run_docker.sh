#!/bin/bash

# checking all processes
./process_checks.sh "docker"

if ./process_checks.sh | grep -q '✗'; then
	echo "Exiting the program now."
	exit 0
fi

# running docker
while true; do
	read -p "The Dockerfile and docker-compose.yml files will be run now. Please press 'y' in order to proceed or 'q' to quit running the program: " user_input
	echo

	if [[ "$user_input" == "y" ]]; then
		docker-compose build
		docker-compose up -d
		echo
		echo "Visit Project Assistant at http://localhost:3000"
		echo
		break
	elif [[ "$user_input" == "q" ]]; then
		exit 0
	else
		echo "Invalid input. Please press 'y' to proceed or 'q' to quit running the program."
	fi
done

while true; do
	read -p "Press 'd' in order to stop the program and remove the Docker image: " down
	if [[ "$down" == "d" ]]; then
		docker-compose down -v
		docker rmi $(docker images | awk '{print $1}' | awk 'NR==2')
		break
	else
		echo "Invalid input. Please press 'd' to stop the program."
	fi
done
exit 0
