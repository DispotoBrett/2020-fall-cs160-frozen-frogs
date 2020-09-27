# Frozen Frogs 🐸 
## Campus Bookshare 📚
***🚧This page is under construction🚧***


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
- Run the script following script AS ROOT! /backend/init-db.sh
	- This will create a user `frogs`
	- Sets the password to `frogs`
	- Creates a database named `frogs`
	- The script will likley prompt you for your mysql root passsword you set earlier. ABOUT 4 times, so just keep  typing it.
	- Feel free to do this by hand. Just make sure the credentals match up.
- Run `python manage.py migrate` to migrate the existing django services to the new database
- Run `python manage.py makemigrations app` and `python manage.py migrate` again to put the models in the database
- Verify everything worked. Your mysql database frogs should be populated
- You can now play around with the database API django made for us.
    - Run `python manage.py shell`
    - Once in the shell `from app.models import Posting`
    - Then you can test commands such as `Posting.objects.All()` see the [django database api reference](https://docs.djangoproject.com/en/3.1/topics/db/queries/) for more info.
    - Django has also has a nice explanation of the ORM [here](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)


## Notes
- The django admin username and password are both `frogs`

## Run in development mode:
To run the django app in deveopment mode:
- Change to the `backend/` directory

- run `python manage.py runserver`

- navigate to `localhost:8000` in your broswer


## Deploy
To deploy the application on an apache web server:
- install and configure both `apache2` and `apache2-dev` (on debian and ubuntu) or equivalent packages

- (Follow the instructions on installing and configuring [mod_wsgi](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/). It will invovle installing a few packages and messing with a few config files. 



