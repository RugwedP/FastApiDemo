from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.student_model import Student
routes = APIRouter()


@routes.get("/fetch")
def fetch_student():

    student_list = [
        {"id": 101, "name": "Nayan", "location": "Kolhapur"},
        {"id": 102, "name": "Rugved", "location": "Kolhapur"},
        {"id": 103, "name": "Hari", "location": "Kolhapur"}
    ]
    return JSONResponse(
        content={
            "student_data" : student_list
        },
        status_code=200
    )

@routes.post("/add")
def add_student(student:Student):

    return JSONResponse(
        status_code=201,
       content={
           "message" : "student Added successfully"
       }
    )