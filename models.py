from sqlalchemy import Boolean, Integer, Column, String
# from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    date = Column(String, index=True)
    