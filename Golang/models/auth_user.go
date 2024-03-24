package models

import "gorm.io/gorm"

type AuthUser struct {
	gorm.Model
	Username  string `gorm:"size:255;not null;unique" json:"username"`
	Password  string `gorm:"size:255;not null;" json:"password"`
	email     string `gorm:"size:255;not null;unique" json:"email"`
	is_active bool   `" json:"is_active"`
}
