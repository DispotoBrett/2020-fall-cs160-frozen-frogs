# Frozen Frogs Campus Bookshare 📚 
SJSU bookshare is a craigslist-like web application for SJSU students to buy and sell their textbooks.

**Note: the docker image `tar` file is in the google docs. Alternatively you can follow the docker build guide in [SETUP.md](https://github.com/DispotoBrett/2020-fall-cs160-frozen-frogs/blob/master/SETUP.md)**

**Note: There is also a user guide / FAQ [here](https://github.com/DispotoBrett/2020-fall-cs160-frozen-frogs/blob/master/UserGuideFAQ.PDF).**
* 1. [Build Prerequisites:](#BuildPrerequisites)
* 2. [Building the dev environment](#Buildingthedevenvironment)
* 3. [Database setup](#Databasesetup)
* 4. [⚠ Database migrations ⚠](#Databasemigrations)
* 5. [Docker Setup 🐳](#DockerSetup)
	* 5.1. [Docker CLI Quick Reference](#DockerCLIQuickReference)
	* 5.2. [Configured Containers (docker-compose.yml)](#ConfiguredContainersdocker-compose.yml)
* 6. [Run in development mode](#Runindevelopmentmode)
* 7. [Deploy](#Deploy)
* 8. [Tips and Tricks](#Notes)
* 9. [Default Configurations](#Defaultconfigurations)
* 10. [Unit Tests](#UnitTests)
* 11. [Regression Tests](#RegressionTests)

##  1. <a name='BuildPrerequisites'></a>Build Prerequisites:
- Python 3.5+ installed

- Python [venv](httpNs://docs.python.org/3/library/venv.html) installed 

- bash or zsh 

- MySQL 8

##  2. <a name='Buildingthedevenvironment'></a>Building the dev environment

- Clone the repository

- Change to the `backend/` directory and run the command: `source install.sh`. This will do three things:
	1. Creates the python virtual environment if it doesn't exist 
	2. activates the virtual environment for your shell session 
	3. installs the app dependencies via `pip` from the `requirements.txt` file.

##  3. <a name='Databasesetup'></a>Database setup

Ubuntu 20.04
- Ensure you have the latest pip dependencies and are on the project venv
- install the following (Ubuntu 20.04):
	- `mysql-client`
	- `mysql-server`
	- `libmysqlclient-dev`
	- `python3-dev`
- First, you'll probably want to delete all the migrations in `backend/app/migrations` if there is any. These were not meant to be shared among team members but this was an oversight in the inital design.
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

##  4. <a name='Databasemigrations'></a>⚠ Database migrations ⚠
If something gets severely messed up or you just want to start with a fresh database:
- `drop` your frogs database
- Delete all the migrations  `rm -rf /backend/app/migrations/*`
- rerun the init db script
- Make sure you're on the venv, as with everythign else we do
- `./manage.py makemigrations`
- `./manage.py migrate`
- Make sure the above worked, then continue below
- `./manage.py makemigrations app`
- `./manage.py migrate`

Upon database schema changes, you'll have to do the following, maybe.
Warning: this will delete the data in your tables. 
- Make sure you have the latest version of the app. You must run `source install.sh` from `/backend`, because this procedure invovles using the `django-extensions` addon
- `python manage.py reset_db --router=default`
- `python manage.py makemigrations`
- `python manage.py migrate`

if you need the app specific tables, youc can run
- `python manage.py migrate app`

If you dont want to lose your data, upon any change to the models, you can try the following, but it will likley cause more issues:
- `python manage.py makemigrations`
- `python manage.py migrate --fake app`
- When django asks, try to allow a None value in a new field

##  5. <a name='DockerSetup'></a>Docker Setup 🐳
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- After installing, you will have access to the docker command line utility, `docker`
- Change to the project root, and run `docker build .`
- Once the container builds, note the image name, and run: `docker run -d -p 8000:8000 <image>`
- Now the app will be running at `localhost:8000`


##  6. <a name='Runindevelopmentmode'></a>Run in development mode:
To run the django app in deveopment mode:
- Change to the `backend/` directory

- run `python manage.py runserver`

- navigate to `localhost:8000` in your broswer

##  7. <a name='Deploy'></a>Deploy
To deploy the application on an apache web server:
- install and configure both `apache2` and `apache2-dev` (on debian and ubuntu) or equivalent packages

- (Follow the instructions on installing and configuring [mod_wsgi](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/). It will invovle installing a few packages and messing with a few config files. 

##  8. <a name='Notes'></a>Tips and Tricks
- Create an admin account by running `python manage.py createsuperuser` and following the prompt

##  9. <a name='Defaultconfigurations'></a>Default Configurations
- By default, there will be 5 books loaded into the tables with negative PKs
	- These are for demo purposes.
- There will also be 2 demo users you can login as:
	1. Username: DemoSeller
	2. Username: DemoBuyer
	- The password for both is 'sjsu' (no quotes)
##  10. <a name='UnitTests'></a>Unit Tests
To run unit tests for the models and views, you can run `./manage.py test`.
##  11. <a name='RegressionTests'></a>Regression Tests
- The system-level automated tests use the following tools:
	- `npm` and `node` for most things
	- `mocha` for the test framework
	- `selenium` for remote webdriver 
	- `msedgewebdriver` for controlling microsoft edge
- The `test-automation/` directory is the home of our regression test node application
	- After `npm install` you can run the tests with `npm test`. Make you startup the django server first at `localhost:8000`
- The tests themselves are in 	`/test-automation/tests/all.test.js`
- There are several node modules in `/test-automation/pages/`. The each provide a factory function for page-object-model (POM) pages/objects. Below is a architectual diagram of the POM model. ![Pom model](https://miro.medium.com/max/1200/1*Uz0xBEbnd7IhEubY392Cow.png)

### The tests
1. Logging in with an actual user
2. Logging in with a non-existent user
3. Registering with all valid credentials
4. Registering with invalid password length, special characters.
5. Registering with non-matching password and confirm password
6. Registering with non-sjsu email address
7. Liking a book and having that reflected on the “browse books” page
8. Un-liking a book and having that reflected
9. Liking books and making sure they show up on the users profile page
10. Posting a valid book listing
11. Posting an invalid book listing (all cases)

