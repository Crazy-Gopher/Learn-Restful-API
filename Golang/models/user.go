package models

import (
	"errors"

	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	FirstName string `json:"firstname"`
	LastName  string `json:"lastname"`
}

type UserRequest struct {
	FirstName string `json:"firstname"`
	LastName  string `json:"lastname"`
}

func (u *UserRequest) Validate() error {
	if u.FirstName == "" {
		return errors.New("required firstname")
	}
	if u.LastName == "" {
		return errors.New("required lastname")
	}
	return nil
}
