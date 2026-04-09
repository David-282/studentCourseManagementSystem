

from pydantic import BaseModel

from models.role import Role


class User(BaseModel):
    name:str
    email:str
    role:Role
    phone_number:str
