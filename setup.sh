#! /bin/bash

# Setup File 
# This file will setup the project for you
# It will install all the dependencies and run the server
# run shell commands 
echo "Setting Up the Project" 
pip3 install django
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py makemigrations ecom
python3 manage.py migrate ecom
python3 manage.py migrate
python3 seed.py 
python3 manage.py runserver 0:8000
