package controllers

import (
	"net/http"
	"userapp/models"
	"userapp/token"

	"github.com/gin-gonic/gin"
	"golang.org/x/crypto/bcrypt"
)

type RegisterInput struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

type LoginInput struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

func (server *Server) Register(ctx *gin.Context) {
	var input RegisterInput
	if err := ctx.ShouldBindJSON(&input); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(input.Password), bcrypt.DefaultCost)
	if err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	user := models.AuthUser{Username: input.Username, Password: string(hashedPassword)}
	server.DB.Create(&user)
	ctx.JSON(http.StatusOK, gin.H{"message": "Registration Successful"})
}

func (server *Server) Login(ctx *gin.Context) {
	var input LoginInput
	if err := ctx.ShouldBindJSON(&input); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	var user models.AuthUser
	if err := server.DB.Where("username = ?", input.Username).First(&user).Error; err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": "Invalid Username or Password"})
		return
	}
	if err := VerifyPassword(input.Password, user.Password); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": "Invalid Username or Password"})
		return
	}
	token, err := token.GenerateToken(user.ID)

	if err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	ctx.JSON(http.StatusOK, gin.H{"Token": token})
}

func VerifyPassword(password, hashedPassword string) error {
	return bcrypt.CompareHashAndPassword([]byte(hashedPassword), []byte(password))
}
