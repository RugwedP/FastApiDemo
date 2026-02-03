from fastapi import FastAPI
from routes import student,teacher




app = FastAPI()

app.include_router(student.routes,prefix="/student")
app.include_router(teacher.routes,prefix="/teacher")

@app.get("/")
def root_request():
    return "This is root request"

