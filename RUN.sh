#!/bin/bash

echo "Welcome to running Project Assistant!"

# checking if ports are free
netstat_port_5432=$(netstat -an --tcp | grep ':5432 ')
ss_port_5432=$(ss -tuln | grep ':5432 ')
netstat_port_3000=$(netstat -an --tcp | grep ':3000 ')
ss_port_3000=$(ss -tuln | grep ':3000 ')

if [[ -z "$netstat_port_3000" || -z "$ss_port_3000" ]]; then
	echo "***Port 3000 is free***"
else
	echo "A process seems to be running on port 3000. Please stop the process before starting the script again."
	exit 0
fi

if [[ -z "$netstat_port_5432" || -z "$ss_port_5432" ]]; then
	echo "***Port 5432 is free***"
else
	echo "A process seems to be running on port 5432. Please stop the process before starting the script again."
	exit 0
fi
echo

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

