package controllers

import (
	"net/http"
	"userapp/models"

	"github.com/gin-gonic/gin"
)

func (server *Server) HealthCheck(ctx *gin.Context) {
	ctx.JSON(http.StatusOK, gin.H{"Status": "Up"})
}

func (server *Server) GetUsers(ctx *gin.Context) {
	var users []models.User
	server.DB.Find(&users)
	ctx.JSON(http.StatusOK, gin.H{"data": users})
}

func (server *Server) CreateUser(ctx *gin.Context) {
	var input models.UserRequest
	if err := ctx.ShouldBindJSON(&input); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	err := input.Validate()
	if err != nil {
		ctx.JSON(http.StatusUnprocessableEntity, gin.H{"error": err.Error()})
		return
	}
	user := models.User{FirstName: input.FirstName, LastName: input.LastName}
	server.DB.Create(&user)
	ctx.JSON(http.StatusOK, gin.H{"data": user})
}

func (server *Server) UpdateUser(ctx *gin.Context) {
	var user models.User
	if err := server.DB.Where("id = ?", ctx.Param("id")).First(&user).Error; err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": "User not found"})
		return
	}
	var input models.UserRequest
	if err := ctx.ShouldBindJSON(&input); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	server.DB.Model(&user).Updates(input)
	ctx.JSON(http.StatusOK, gin.H{"data": user})
}

func (server *Server) GetUser(ctx *gin.Context) {
	var user models.User
	if err := server.DB.Where("id = ?", ctx.Param("id")).First(&user).Error; err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"data": "User not found"})
		return
	}
	ctx.JSON(http.StatusOK, user)
}

func (server *Server) DeleteUser(ctx *gin.Context) {
	var user models.User
	if err := server.DB.Where("id = ?", ctx.Param("id")).First(&user).Error; err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"data": "User not found"})
		return
	}
	server.DB.Delete(&user)
	ctx.JSON(http.StatusOK, user)
}
