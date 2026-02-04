from pydantic import BaseModel


class Teacher(BaseModel):

    id:int
    name:str
    location:str
    email:str   
    is_active:bool = True
