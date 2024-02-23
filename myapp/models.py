from .database import Base
from sqlalchemy import Column, String, Integer, Boolean


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    departement = Column(String, nullable=True)
    roll_no = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=True)
