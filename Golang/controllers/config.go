package controllers

import (
	"fmt"
	"log"
	"os"
	"userapp/models"

	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func loadEnv() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
}

func (server *Server) ConnectDB() {
	loadEnv()
	dbDriver := os.Getenv("DB_DRIVER")
	dbHost := os.Getenv("DB_HOST")
	dbUser := os.Getenv("DB_USER")
	dbPass := os.Getenv("DB_PASSWORD")
	dbName := os.Getenv("DB_NAME")
	dbPort := os.Getenv("DB_PORT")
	var err error
	if dbDriver == "postgres" {
		dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=disable TimeZone=Asia/Kolkata", dbHost, dbUser, dbPass, dbName, dbPort)
		server.DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})

		if err != nil {
			panic(fmt.Sprintf("Failed to connect to PostgreSQL database! %s", dsn))
		}
	}
}

func (server *Server) DisconnectDB() {
	dbSQL, err := server.DB.DB()
	if err != nil {
		panic("Failed to kill connection from database")
	}
	dbSQL.Close()
}

func (server *Server) MigrateDB() {
	err := server.DB.AutoMigrate(&models.User{}, &models.AuthUser{})
	if err != nil {
		panic("Unable to apply the migrations")
	}
}
