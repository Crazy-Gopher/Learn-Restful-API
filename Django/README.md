## Steps to Setup Django Application(Without Docker-Compose):

1. Create Virtual Env
python -m venv venv

2. Activate Virtual ENV
.\venv\Scripts\activate

3. Install the requirements
pip install -r .\requirements.txt

4. Run postgresql
docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=postgres -d postgres:16
docker exec -it postgres bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"


5. If you are running outside the container then change the HOST from "postgres" to "localhost" in the DATABASES.

6. Apply migrations (Create Table and Super user)
python manage.py migrate
python manage.py createsuperuser

7. Run the server
python manage.py runserver 8000

deactivate


## Steps to Setup Django Application(With Docker-Compose):

1. If you are running outside the container then change the HOST from "postgres" to "localhost" in the DATABASES.
2. Run the docker-compose
docker-compose up --build

or
docker-compose up -d --build
docker attach userapp


2. Apply the migrations
docker exec -it userapp bash
python manage.py migrate

3. Stop the containers
docker-compose down





# Create Django Project
django-admin startproject main


Get-ExecutionPolicy
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force


Add db connection in settting file
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":"postgres",
        "USER":"postgres",
        "PASSWORD":"postgres",
        "HOST":"127.0.0.1",
        "PORT":"5432"
    }
}



python manage.py startapp user

Add app in INSTALLED_APP

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user'
]

python manage.py makemigrations



psql commands:
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
create database django;
\l - list databases
\dt - list tables
\c database_name  - change database


## Unittest cases
python -m coverage run -m pytest .
coverage report -m


# Precommit
pip install pre-commit
pre-commit install
pre-commit run --all-files
git commit -m "your commit message" --no-verify