## Steps to Setup FastAPI Application(With Docker-Compose):
1. Run the docker-compose
docker-compose up --build

or
docker-compose up -d --build
docker attach web

2. Stop the containers
docker-compose down

>**Note** If the the error fastapi database does not exits, run the below commands to create databse
docker exec -it postgres_golang bash
psql "host=127.0.0.1 port=5432 user=postgres dbname=postgres"
CREATE DATABASE gin;


Notes:
1. Golang api use authentications.(JWT authentication, Register and Login API)
2. User resource fields match Django, FastAPI, and Flask: username, password, email, is_active
3. PATCH `/api/v1/users/:id` is available for partial updates



## Other importent Notes

go mod init <github-link>
go mod init userapp
go get github.com/gin-gonic/gin gorm.io/gorm
go get github.com/joho/godotenv
go get -u gorm.io/driver/postgres



other dev - go mod download

DBMate for migration

Cannot define new methods on non-local type controllers.Server

go get -u github.com/dgrijalva/jwt-go
go get -u golang.org/x/crypto
