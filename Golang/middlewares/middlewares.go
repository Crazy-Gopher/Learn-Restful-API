package middlewares

import (
	"log"
	"net/http"
	"time"
	"userapp/token"

	"github.com/gin-gonic/gin"
)

func Logger() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		log.Print("main started")
		t := time.Now()
		// before request
		ctx.Next() // Original Request
		// after request
		latency := time.Since(t)
		log.Print(latency)
		status := ctx.Writer.Status()
		log.Println(status)
		log.Print("main ended")
	}
}

func JwtAuthMiddleware() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		err := token.TokenValid(ctx)
		if err != nil {
			ctx.String(http.StatusUnauthorized, "Unauthorized")
			ctx.Abort()
			return
		}
		ctx.Next()
	}
}
