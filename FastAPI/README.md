# Steps to Setup Fast API Application (Without Docker-compose)

1. Create Virtual Environment
python -m venv venv
.\venv\Scripts\activate

2. Install the requirements
pip install fastapi uvicorn sqlalchemy psycopg2-binary
pip install -r requirements.txt

3. Start the PostgreSQL container and Create Database
docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=postgres -d postgres
docker exec -it postgres bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
CREATE DATABASE fastapi;

4. Run the Application
uvicorn main:app --port 8001 --reload


## Steps to Setup FastAPI Application(With Docker-Compose):
1. Run the docker-compose
docker-compose up --build

or
docker-compose up -d --build
docker attach userapp

2. Stop the containers
docker-compose down

>**Note** If the the error fastapi database does not exits, run the below commands to create databse
docker exec -it postgres bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
CREATE DATABASE fastapi;


## psql commands:
\l - list databases
\dt - list tables
\c database_name  - change database
\q - Quit
\x - extended mode on or off