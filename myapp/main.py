from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from . import schemas, models, database
from fastapi import status


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/data/", status_code=status.HTTP_200_OK)
def get_data(db: Session = Depends(get_db)):
    query = db.query(models.Student).all()
    return {"data": query}

@app.post("/data/post/" ,status_code=status.HTTP_201_CREATED, response_model = schemas.StudentCreate)
def create_student(requst: schemas.StudentCreate, db: Session=Depends(get_db)):
    new_student = models.Student(name=requst.name, departement=requst.departement, email=requst.email, roll_no=requst.roll_no, id=requst.id)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.put('/data/put/{id}', status_code=status.HTTP_202_ACCEPTED)
def put_data(id: int, request: schemas.StudentCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        return {"error": "Student not found"}
    for key, value in request.dict().items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return {"message": "Student updated successfully"}

@app.delete('/data/delete/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_data(id:int, db: Session=Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id==id).first()
    if student:
        db.delete(student)
        db.refresh(student)
        return "Student is Deleted successfully"
    return "Student Is Not Found"



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}








