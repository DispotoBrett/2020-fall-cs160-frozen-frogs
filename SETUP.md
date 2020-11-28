# Deploying the application
By Far, the easiet way to run this application is through a docker container. 
We've procured a few scripts and a dockerfile to get the app running in just two commands.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) (or `docker.io` on linux machines)
2. After installing, you will have access to the docker command line utility, `docker`. Make sure the docker dameon is running.
3. Change to the project root, and run `docker build .`
4. Once the container builds, note the image name, and run: `docker run -d -p 8000:8000 <image>`
5. Now the app will be running at `localhost:8000`
6. Enjoy!

