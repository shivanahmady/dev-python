#!/bin/sh
export FLASK_APP=./main.py
source env/bin/activate
#export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
# export APP_SETTINGS="development"
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run

