from fastapi import FastAPI
from routes import student,teacher

from database import engine, SessionLocal
from database_model.student import Student
from database_model.teacher import Teacher


from database import Base
# this is test
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(student.routes,prefix="/student")
app.include_router(teacher.routes,prefix="/teacher")

@app.get("/")
def root_request():
    return "This is root request"

