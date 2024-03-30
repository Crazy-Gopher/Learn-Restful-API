from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from user.crud_user import get_users, create_user, get_user, update_user, partial_update_user, delete_user
from typing import List, Optional
from user.schemas import ResponseUser, UpdateRequestUser, RequestUser

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.get("/", status_code=200, response_model= List[ResponseUser])
def users(db: Session = Depends(get_db)):
    return get_users(db)

@router.post("/", status_code=201, response_model= ResponseUser)
def users(request: RequestUser, db: Session = Depends(get_db)):
    return create_user(request, db)

@router.get("/{id}", status_code=200, response_model= ResponseUser)
def users(id: int, db: Session = Depends(get_db)):
    return get_user(id, db)

@router.put("/{id}", status_code=200, response_model= ResponseUser)
def users(id: int, request: RequestUser, db: Session = Depends(get_db)):
    return update_user(id, request, db)

@router.patch("/{id}", status_code=200, response_model= ResponseUser)
def users(id: int, request : Optional[UpdateRequestUser]={}, db: Session = Depends(get_db)):
    return partial_update_user(id, request, db)

@router.delete("/{id}", status_code=204)
def users(id: int, db: Session = Depends(get_db)):
    return delete_user(id, db)
