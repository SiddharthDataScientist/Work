from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, Sessionloacal
from sqlalchemy.orm import Session
from models import User

app = FastAPI()

models.Base.metadata.create_all(bind= engine)

def get_db():
    try: 

       db = Sessionloacal()
       yield db

    
    finally:
        db.clsoe()

@app.get("/")
async def read_all(db:Session = Depends(get_db)):
    return db.query(models.User).all()




