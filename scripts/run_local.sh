#!/bin/bash

source ../.env

postgres_admin_access(){
	printf "An existing postgres user account with admin privileges will be necessary to create the database.\nYour username and password will be saved in a .pgpass file for the connection, and will be removed after the script finishes.\n"
	while true; do
		read -p "Please provide your postgres username: " postgres_admin_username

		if [[ -n "$postgres_admin_username" ]]; then
			break
		else
			echo "Input cannot be empty."
		fi
	done
	while true; do
		read -s -p "Please provide the password: " postgres_admin_password

		if [[ -n "$postgres_admin_password" ]]; then
			break
		else
			echo "Input cannot be empty."
		fi
	done

	# .pgpass TO BE DELETED AFTER SCRIPT
	echo "localhost:5432:*:$postgres_admin_username:$postgres_admin_password" > ~/.pgpass
	chmod 600 ~/.pgpass

	# .env LINES TO BE DELETED AFTER SCRIPT
	env_db_username="DB_USERNAME=$postgres_admin_username"
	env_db_password="DB_PASSWORD=$postgres_admin_password"
	if ! grep -q "$env_db_username" .env; then
		echo "$env_db_username" >> .env
	fi
	if ! grep -q "$env_db_password" .env; then
		echo "$env_db_password" >> .env
	fi
}

if [ -a "../.venv" ]; then
	echo "venv already exists, only installing dependencies..."
	cd ..
	source .venv/bin/activate
	pip install -q -r requirements.txt
	postgres_admin_access
	psql -U "$DB_USERNAME" -h "localhost" -c "CREATE DATABASE pa_db;"
	python3 main.py
	rm ~/.pgpass
else
	echo "creating venv and installing dependencies..."
	cd ..
	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
fi

echo "success local"
