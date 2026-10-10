## Steps to Setup Flask Application(Without Docker-Compose):

1. Create Virtual Env
python -m venv venv

2. Activate Virtual ENV
.\venv\Scripts\activate

3. Install the requirements
pip install -r .\requirements.txt

4. Run postgresql
docker run -p 5432:5432 --name postgres_flask -e POSTGRES_PASSWORD=postgres -d postgres:16
docker exec -it postgres_flask bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
create database flask;

5. If you are running outside the container then change the HOST from "postgres_flask" to "127.0.0.1" in config.py.

6. Run the server
set FLASK_APP=app
python -m flask run -p 8002 --reload

deactivate


## Steps to Setup Flask Application(With Docker-Compose):
1. Run the docker-compose
docker-compose up --build

or
docker-compose up -d --build
docker attach userapp_flask

2. Stop the containers
docker-compose down

>**Note** If the flask database does not exist, run the below commands to create database
docker exec -it postgres_flask bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
CREATE DATABASE flask;


## psql commands:
\l - list databases
\dt - list tables
\c database_name  - change database
\q - Quit
\x - extended mode on or off
