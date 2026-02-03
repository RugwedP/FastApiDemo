from pydantic import BaseModel


class Student(BaseModel):

    id:int
    name:str
    location:str
    email:str   
    is_active:bool = True
