## Steps to Setup Flask Application(Without Docker-Compose):

1. Create Virtual Env
python -m venv venv

2. Activate Virtual ENV
.\venv\Scripts\activate

3. Install the requirements
pip install -r .\requirements.txt
pip install flask_sqlalchemy

4. Run postgresql
docker run -p 5432:5432 --name postgres_flask -e POSTGRES_PASSWORD=postgres -d postgres:16
docker exec -it postgres_flask bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
create database flask;

5. If you are running outside the container then change the HOST from "postgres" to "localhost" in the DATABASES.

6. Run the server
set FLASK_APP=app
python -m flask run -p 8002 --reload

deactivate


## Steps to Setup Flask Application(With Docker-Compose):
