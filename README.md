# Frozen Frogs 🐸 
## Campus Bookshare 📚
***🚧This page is under construction🚧***


## Build Prerequisites:
- Python 3.5+ installed

- Python [venv](https://docs.python.org/3/library/venv.html) installed 

- bash or zsh 

- MySQL *(version TBD)*

## Building the dev environment 

- Clone the repository

- Change to the `backend/` directory and run the command: `source install.sh`. This will do three things:
	1. Creates the python virtual environment if it doesn't exist 
	2. activates the virtual environment for your shell session 
	3. installs the app dependencies via `pip` from the `requirements.txt` file.

## Run in development mode:
To run the django app in deveopment mode:
- Change to the `backend/` directory

- run `python manage.py runserver`

- navigate to `localhost:8000` in your broswer

## Deploy
To deploy the application on an apache web server:
- install and configure both `apache2` and `apache2-dev` (on debian and ubuntu) or equivalent packages

- (Follow the instructions on installing and configuring [mod_wsgi](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/). It will invovle installing a few packages and messing with a few config files. 
