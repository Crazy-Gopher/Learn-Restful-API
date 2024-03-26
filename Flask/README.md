## Steps to Setup Django Application(Without Docker-Compose):

1. Create Virtual Env
python -m venv venv

2. Activate Virtual ENV
.\venv\Scripts\activate

3. Install the requirements
pip install -r .\requirements.txt
pip install flask_sqlalchemy

4. Run postgresql
docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=postgres -d postgres
docker exec -it postgres bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
create database flask;

5. If you are running outside the container then change the HOST from "postgres" to "localhost" in the DATABASES.

6. Run the server
set FLASK_APP=app
python -m flask run -p 8002 --reload

deactivate


## Steps to Setup Django Application(With Docker-Compose):

1. Run the docker-compose
docker-compose up --build

or
docker-compose up -d --build
docker attach userapp

2. Apply the migrations
docker exec -it userapp bash
python manage.py migrate

3. Stop the containers
docker-compose down
