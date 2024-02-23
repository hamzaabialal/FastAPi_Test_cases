from .models import Student
from pydantic import BaseModel


class StudentCreate(BaseModel):
    id: int
    name: str
    departement: str
    email: str
    roll_no: int


    class Config:
        orm_mode = True


class StudentBase(StudentCreate):
    class Config:
        orm_mode =True