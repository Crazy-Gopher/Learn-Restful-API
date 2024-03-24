package main

import (
	"userapp/controllers"
	"userapp/middlewares"

	"github.com/gin-gonic/gin"
)

var server = controllers.Server{}

func main() {
	server.ConnectDB()
	defer server.DisconnectDB()
	server.MigrateDB()
	initializeRoutes()
}

func initializeRoutes() {
	server.Router = gin.Default()
	server.Router.Use(middlewares.Logger())
	server.Router.GET("/healthcheck", server.HealthCheck)

	private := server.Router.Group("/api/v1")
	private.Use(middlewares.JwtAuthMiddleware())
	private.GET("/users", server.GetUsers)
	private.POST("/users", server.CreateUser)
	private.PUT("/users/:id", server.UpdateUser)
	// Please add patch api as well
	// private.PATCH("/users/:id", server.UpdateUser)
	private.GET("/users/:id", server.GetUser)
	private.DELETE("/users/:id", server.DeleteUser)

	public := server.Router.Group("/api")

	public.POST("/register", server.Register)
	public.POST("/login", server.Login)

	err := server.Router.Run(":8080")
	if err != nil {
		return
	}
}
