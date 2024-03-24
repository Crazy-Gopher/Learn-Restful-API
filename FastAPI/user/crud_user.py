from user.models import User
from sqlalchemy.orm import Session
from user.schemas import RequestUser, UpdateRequestUser, ResponseUser
from fastapi import HTTPException, status

def get_users(db: Session):
    user = db.query(User).all()
    return user

def create_user(request:RequestUser, db: Session) -> ResponseUser:
    user = db.query(User).filter(User.email == request.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with email already exists.")
    new_user = User(username=request.username, email=request.email, password=request.password, is_active=request.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session) -> ResponseUser:
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with email already exists.")
    return user

def update_user(id: int, request: RequestUser, db: Session) -> ResponseUser:
    user = db.query(User).filter(User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with id does not exists.")
    user.update(request.model_dump())
    db.commit()

    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with id does not exists.")
    return user

def partial_update_user(id: int, request: UpdateRequestUser, db: Session) -> ResponseUser:
    if request:
        update_data = request.model_dump(exclude_unset=True)
        if update_data:
            user = db.query(User).filter(User.id == id)
            if not user.first():
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user with id does not exists.")
            user.update(update_data)
            db.commit()

    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user with id does not exists.")
    return user

def delete_user(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user with email already exists.")
    db.delete(user)
    db.commit()
    return "deleted"