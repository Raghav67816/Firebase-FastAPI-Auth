from typing import Optional
from pydantic import BaseModel

class NewUser(BaseModel):
    name: str
    email: str
    password: str
    phone_number: str


class UserLogin(BaseModel):
    email: str
    password: str


class EmailAndToken(BaseModel):
    email: str
    token: str
