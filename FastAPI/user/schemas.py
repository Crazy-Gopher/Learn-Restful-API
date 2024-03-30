from pydantic import BaseModel

class BaseUser(BaseModel):
    email: str
    username: str
    password: str
    is_active: bool

class RequestUser(BaseUser):
    class Config():
        orm_mode = True

class UpdateRequestUser(BaseModel):
    email: str = ""
    username: str = ""
    password: str = ""
    is_active: bool = False

class ResponseUser(BaseUser):
    id: int

    class Config():
        orm_mode = True
