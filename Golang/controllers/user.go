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
	var existing models.User
	if err := server.DB.Where("email = ?", input.Email).First(&existing).Error; err == nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": "user with email already exists"})
		return
	}
	user := models.User{
		Username: input.Username,
		Password: input.Password,
		Email:    input.Email,
		IsActive: input.IsActive,
	}
	server.DB.Create(&user)
	ctx.JSON(http.StatusCreated, gin.H{"data": user})
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
	err := input.Validate()
	if err != nil {
		ctx.JSON(http.StatusUnprocessableEntity, gin.H{"error": err.Error()})
		return
	}
	server.DB.Model(&user).Select("Username", "Password", "Email", "IsActive").Updates(models.User{
		Username: input.Username,
		Password: input.Password,
		Email:    input.Email,
		IsActive: input.IsActive,
	})
	ctx.JSON(http.StatusOK, gin.H{"data": user})
}

func (server *Server) PatchUser(ctx *gin.Context) {
	var user models.User
	if err := server.DB.Where("id = ?", ctx.Param("id")).First(&user).Error; err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": "User not found"})
		return
	}
	var input models.PatchUserRequest
	if err := ctx.ShouldBindJSON(&input); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	updates := map[string]interface{}{}
	if input.Username != nil {
		updates["username"] = *input.Username
	}
	if input.Password != nil {
		updates["password"] = *input.Password
	}
	if input.Email != nil {
		updates["email"] = *input.Email
	}
	if input.IsActive != nil {
		updates["is_active"] = *input.IsActive
	}
	if len(updates) > 0 {
		server.DB.Model(&user).Updates(updates)
	}
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
