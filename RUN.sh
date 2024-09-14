#!/bin/bash
# setting env variables
echo "Welcome to running Project Assistant!"
echo "You will now be prompted to set your environmental variables, which are necessary to run the program."
echo

read -p "Please enter your Postgres username: " db_username
read -p "Please enter your Postgres password: " db_password

echo "DB_USERNAME='$db_username'" >> .env
echo "DB_PASSWORD='$db_password'" >> .env
echo "DB_PORT=5432" >> .env
echo "SECRET_KEY='secret_key'" >> .env
echo
echo '***The .env file has been created.***'
echo
# running docker
read -p "The Dockerfile and docker-compose.yml files will be run now. Please press 'y' in order to proceed: " user_input

if [[ "$user_input" == "y" ]]; then
	docker-compose build
	docker-compose up -d
	echo
	echo "Visit Project Assistant at http://localhost:3000"
	read -p "Press 'd' in order to stop the container and remove the image: " down
	if [[ "$down" == "d" ]]; then
		docker-compose down
		docker rmi $(docker images | awk '{print $1}' | awk 'NR==2')
	fi
else
	echo "Exiting the program now."
	exit
fi

