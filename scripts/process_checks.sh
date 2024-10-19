#!/bin/bash

ports=(3000 5432)
netstat_port=""
netstat=$(command -v netstat)
lsof=$(command -v lsof)

# checking ports
confirm_ports () {
	if [[ "$3" == "local" && "$2" == "5432" ]]; then
		if [[ -z "$1" ]]; then
			echo "✗ Error: postgres service is not running on port $2. Please start postgres service before running the script again."
			exit 1
		else
			echo "✓ port $2 is not free"
		fi
	elif [[ -z "$1" ]]; then
		echo "✓ port $2 is free"
	else
		echo "✗ Error: A process seems to be running on port $2. Please stop the process before running the script again."
		exit 1
	fi
}

for port in "${ports[@]}"; do
	if [[ "$1" == "Linux" || "$1" == "Windows" ]]; then
		if [[ -n "$netstat" ]]; then
			netstat_port=$(netstat -an --tcp | grep ":$port ")
		fi

		confirm_ports "$netstat_port" "$port" "$2"
	elif [[ "$1" == "Darwin" ]]; then
		if [[ -n "$lsof" ]]; then
			netstat_port=$(lsof -i tcp:"$port")
		elif [[ -n "$netstat" ]]; then
			netstat_port=$(netstat -an 2>/dev/null | grep ":$port ")
		fi

		confirm_ports "$netstat_port" "$port"
	fi
done

# local
if [[ "$2" == "local" ]]; then
	python3_is=$(python3 --version)
	postgres_is=$(psql --version)

	if [[ -n "$python3_is" ]]; then
		echo "✓ python3 is installed"
	else
		echo "✗ Error: python3 is not installed. Exiting now."
		exit 1
	fi

	if [[ -n "$postgres_is" ]]; then
		echo "✓ postgresql is installed"
	else
		echo "✗ Error: postgresql is not installed. Exiting now."
		exit 1
	fi
fi

# docker
if [[ "$2" == "docker" ]]; then
	docker=$(pgrep -l docker)
	docker_is=$(docker --version)
	docker_compose_is=$(docker-compose --version)

	if [[ -n "$docker_is" ]]; then
		echo "✓ docker is installed"
	else
		echo "✗ Error: Docker is not installed. Exiting now."
		exit 1
	fi

	if [[ -n "$docker_compose_is" ]]; then
		echo "✓ docker-compose is installed"
	else
		echo "✗ Error: Docker-compose is not installed. Exiting now."
		exit 1
	fi

	if [[ -n "$docker" ]]; then
		echo "✓ docker is running"
	else
		echo "✗ Error: Docker is not running. Please make sure to start Docker before running the script again."
		exit 1
	fi
fi







