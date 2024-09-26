#!/bin/bash
ports=(3000 5432)
netstat_port=""
os=$(uname -s)
netstat=$(command -v netstat)
lsof=$(command -v lsof)
docker=$(pgrep -l dockerd)
docker_is=$(docker --version)
docker_compose_is=$(docker-compose --version)

# checking docker and docker-compose
if [[ -n "$docker_is" ]]; then
	echo "✓ Docker is installed"
else
	echo "✗ Error: Docker is not installed."
fi

if [[ -n "$docker_compose_is" ]]; then
	echo "✓ Docker-compose is installed"
else
	echo "✗ Error: Docker-compose is not installed."
fi


# checking docker running
if [[ -n "$docker" ]]; then
	echo "✓ Docker is running"
else
	echo "✗ Error: Docker is not running. Please make sure to start Docker before running the script again."
fi

# checking ports
confirm_ports () {
        if [[ -z "$1" ]]; then
                echo "✓ Port $2 is free"
        else
                echo "✗ Error: A process seems to be running on port $2. Please stop the process before running the script again."
        fi
}

for port in "${ports[@]}"; do
	if [[ "$os" == "Linux" || "$os" == MINGW* || "$os" == MSYS* || "$os" == CYGWIN* || "$os" == MINGW64* ]]; then
		if [[ -n "$netstat" ]]; then
			netstat_port=$(netstat -an --tcp | grep ":$port ")
		fi

		confirm_ports "$netstat_port" "$port"
	elif [[ "$os" == "Darwin" ]]; then
		if [[ -n "$lsof" ]]; then
			netstat_port=$(lsof -i tcp:"$port") 
		elif [[ -n "$netstat" ]]; then
			netstat_port=$(netstat -an 2>/dev/null | grep ":$port ")
		fi

		confirm_ports "$netstat_port" "$port"
	fi
done






