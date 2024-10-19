#!/bin/bash

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
