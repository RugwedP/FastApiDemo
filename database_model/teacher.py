from sqlalchemy import Column,Integer,String,Boolean
from database import Base


class Teacher(Base):

    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    email = Column(String)   
    is_active= Column(Boolean)
