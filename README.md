
# Efish

Welcome on board, this is test task from efishery
## Getting Started
![Context](https://github.com/kunci115/efish/blob/master/Context.jpg) <br>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
Overview of the project that we have 2 apps server running on different port. <br>
![Deployment](https://github.com/kunci115/efish/blob/master/deployment.jpg) <br>
### Prerequisites

What things you need to install the software and how to install them

For Docker Instance:
1. install Docker
2. Your own IDE(vscode/pycharm/etc)

For Local Instance:
1. Install [Python3.9](https://www.python.org/downloads/)
2. install [Node-js](https://nodejs.org/en/download/)

### Installing

A step by step series of examples that tell you how to get a development env running

Step:

```
1. git clone https://github.com/kunci115/efish.git
2. cd efish
3. docker-compose build
4. docker-compose up
5. Get in to the docker efish_coreconnect
6. docker exec -it "efish_coreconnect" /bin/bash
7. python manage.py makemigrations
8. python manage.py migrate

```

Setup without docker on Ubuntu (tested on Ubuntu 20.04):
```
Setting up django-server(coreconnect)
1. git clone https://github.com/kunci115/efish.git
2. cd coreconnect
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver
------------------------------
Setting up node js server(fetcher apps)
1. Open new terminal
2. cd fetcher
3. npm install
4. node index.js
```
If everythings running well, django server will be run on 8000 port,  and node server will be run on 3000 port.


## API Endpoint

Endpoint is specified documented in [api.md](https://github.com/kunci115/efish/blob/master/api.md)

## Authors efish apps

* **Rino Alfian**

Github profile [rino alfian](https://github.com/kunci115)

