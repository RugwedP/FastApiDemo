
from fastapi import APIRouter

routes = APIRouter()


@routes.get("/fetch")
def fetch_student():
    return "Teachers fetched"