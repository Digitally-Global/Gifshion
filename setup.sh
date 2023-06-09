#! /bin/bash

# Setup File 
# This file will setup the project for you
# It will install all the dependencies and run the server
# run shell commands 
echo "Setting Up the Project" 
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python seed.py 
python manage.py runserver