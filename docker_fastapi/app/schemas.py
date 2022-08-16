from typing import List, Dict, Set

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    email: str

class UserCreate(UserBase):
    first_name: str
    last_name: str
    company_name: str
    city_name: str

class UserData(UserBase):
    first_name: str
    last_name: str
    company_name: str
    city_name: str

    class Config:
        orm_mode = True