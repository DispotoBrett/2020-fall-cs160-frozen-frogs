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

- Change to the `backend/` directory and run `install.sh`.  this will create the python virtual environment, and install several  dependencies using `pip`. 

- Next you'll want to activate the python virtual environment by running `source /.venv/bin/activate` from the `backend` directory.

## Run in development mode:
To run the django app in deveopment mode:
- Change to the `backend/` directory

- run `python manage.py runserver`

- navigate to `localhost:8000` in your broswer

## Deploy
To deploy the application on an apache web server:
- install and configure both `apache2` and `apache2-dev` (on debian and ubuntu) or equivalent packages

- (Follow the instructions on installing and configuring [mod_wsgi](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/). It will invovle installing a few packages and messing with a few config files. 
