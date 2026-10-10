package models

import (
	"errors"
)

type User struct {
	ID       uint   `json:"id" gorm:"primaryKey"`
	Username string `json:"username"`
	Password string `json:"password"`
	Email    string `json:"email" gorm:"unique"`
	IsActive bool   `json:"is_active"`
}

type UserRequest struct {
	Username string `json:"username"`
	Password string `json:"password"`
	Email    string `json:"email"`
	IsActive bool   `json:"is_active"`
}

type PatchUserRequest struct {
	Username *string `json:"username"`
	Password *string `json:"password"`
	Email    *string `json:"email"`
	IsActive *bool   `json:"is_active"`
}

func (u *UserRequest) Validate() error {
	if u.Username == "" {
		return errors.New("required username")
	}
	if u.Password == "" {
		return errors.New("required password")
	}
	if u.Email == "" {
		return errors.New("required email")
	}
	return nil
}
