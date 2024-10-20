#!/bin/bash

postgres_admin_login(){
	printf "An existing postgres user account with admin privileges will be necessary to create the user for the Project Assistant database.\nYou may use the default 'postgres' user for this purposes, otherwise any other account with admin privileges will work. Your username or password will not be saved anywhere and only serves to purpose to create the user for the application's database.\n"
	read -p "Please provide your postgres username: " postgres_admin_username
	read -s -p "Please provide the password: " postgres_admin_password
	DB_HOST="localhost"
	DB_PORT="5432"
	DB_USER="$postgres_admin_username"
	DB_PASSWORD="$postgres_admin_password"
	echo "$DB_HOST:$DB_PORT:*:$DB_USER:$DB_PASSWORD" > ../.pgpass
	chmod 600 ../.pgpass
}

if [ -a "../.venv" ]; then
	echo "venv already exists, only installing dependencies..."
	# cd ..
	# source .venv/bin/activate
	# pip install -r requirements.txt
else
	echo "creating venv and installing dependencies..."
	cd ..
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
fi

echo "success local"
