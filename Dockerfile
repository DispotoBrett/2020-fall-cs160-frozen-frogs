FROM ubuntu

#Copy the entire projec to /app
COPY . /app

#This script installs the all of the pip dependencies and
#populates the database with sample data
RUN chmod +x /app/backend/docker-install.sh

#I write on windows so we have to remove \r at newlines
RUN sed -i 's/\r//g' /app/backend/docker-install.sh

#Install dependencies
RUN apt -y update
RUN apt -y install python3  python3-pip libmysqlclient-dev mysql-client	
RUN /app/backend/docker-install.sh

#Setup DB
#RUN python3 /app/backend/manage.py makemigrations 
#RUN python3 /app/backend/manage.py migrate 
#RUN python3 /app/backend/manage.py makemigrations app
#RUN python3 /app/backend/manage.py migrate app
#RUN python3 /app/backend/manage.py migrate 
#RUN python3 /app/backend/manage.py loaddata /app/backend/app/fixtures/defaults.json
