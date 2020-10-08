# Frozen Frogs Campus Bookshare 📚
***🚧This page is under construction🚧***

## Table of contents
- [Frozen Frogs Campus Bookshare 📚](#frozen-frogs-campus-bookshare-)
	- [Table of contents](#table-of-contents)
	- [Build Prerequisites:](#build-prerequisites)
	- [Building the dev environment](#building-the-dev-environment)
	- [Database setup](#database-setup)
	- [⚠ Database migrations ⚠](#-database-migrations-)
	- [Docker Setup](#docker-setup)
	- [Run in development mode:](#run-in-development-mode)
	- [Deploy](#deploy)
	- [Notes](#notes)

## Build Prerequisites:
- Python 3.5+ installed

- Python [venv](https://docs.python.org/3/library/venv.html) installed 

- bash or zsh 

- MySQL 8

## Building the dev environment

- Clone the repository

- Change to the `backend/` directory and run the command: `source install.sh`. This will do three things:
	1. Creates the python virtual environment if it doesn't exist 
	2. activates the virtual environment for your shell session 
	3. installs the app dependencies via `pip` from the `requirements.txt` file.

## Database setup

Ubuntu 20.04
- Ensure you have the latest pip dependencies and are on the project venv
- install the following (Ubuntu 20.04):
	- `mysql-client`
	- `mysql-server`
	- `libmysqlclient-dev`
	- `python3-dev`
- run `/etc/init.d/mysql start`
- run `sudo mysql_secure_installation`
- Follow the prompt. Allow the least secure options available. Don't remove anon users. Don't disable remote root login.
- Login to mysql as root "sudo mysql -u root -p', enter your password
- Run the script following script AS ROOT! `/database/scripts/init-db.sh`
	- This will create a user `frogs`
	- Sets the password to `frogs`
	- Creates a database named `frogs`
	- The script will likley prompt you for your mysql root passsword you set earlier. ABOUT 4 times, so just keep  typing it.
	- Feel free to do this by hand. Just make sure the credentals match up.
    - You might want to run the sqldump script provided in `/database/scripts/loadBooks.sql` to populate with some books
      for a demo.
- Run `python manage.py migrate` to migrate the existing django services to the new database
- Run `python manage.py makemigrations app` and `python manage.py migrate` again to put the models in the database
- Verify everything worked. Your mysql database frogs should be populated
- You can now play around with the database API django made for us.
    - Run `python manage.py shell`
    - Once in the shell `from app.models import Posting`
    - Then you can test commands such as `Posting.objects.All()` see the [django database api reference](https://docs.djangoproject.com/en/3.1/topics/db/queries/) for more info.
    - Django has also has a nice explanation of the ORM [here](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)

## ⚠ Database migrations ⚠
Upon database schema changes, you'll have to do the following.
Warning: this will delete the data in your tables. 
- Make sure you have the latest version of the app. You must run `source install.sh` from `/backend`, because this procedure invovles using the `django-extensions` addon
- `python manage.py reset_db --router=default`
- `python manage.py makemigrations`
- `python manage.py migrate`

If you dont want to lose your data, upon any change to the models, you can try the following, but it will likley cause more issues:
- `python manage.py makemigrations`
- `python manage.py migrate --fake app`
- When django asks, try to allow a None value in a new field

## Docker Setup
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- After installing, you will have access to the docker command line utility, `docker`
- For this project, we will be using Docker Compose, which is a way to streamline running multiple Docker containers from a single config file, docker-compose.yml
- To build and run the docker-compose.yml file, navigate to the project directory and run `docker-compose up -d --build`
- The above command will build the container images as well as run them in the background (-d option specifies detached mode)
- To start and stop the containers, you can use `docker-compose stop` and `docker-compose start`

### Docker CLI Quick Reference
- To display all containers on your system run `docker ps -a`
- To log in to one of your containers run `docker exec -it <container_name> /bash`
- NOTE: Not all containers use the same shell executable. Above we used bash, but depending on the container image, it may be different.

### Configured Containers (docker-compose.yml)
- MySQL container with env options specified in `database/mysql.env`

## Run in development mode:
To run the django app in deveopment mode:
- Change to the `backend/` directory

- run `python manage.py runserver`

- navigate to `localhost:8000` in your broswer

## Deploy
To deploy the application on an apache web server:
- install and configure both `apache2` and `apache2-dev` (on debian and ubuntu) or equivalent packages

- (Follow the instructions on installing and configuring [mod_wsgi](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/). It will invovle installing a few packages and messing with a few config files. 

## Notes
- The django admin username and password are both `frogs`
- Create an admin account by running `python manage.py createsuperuser` and following the prompt
