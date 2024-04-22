from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


origins = ["http://localhost:3000", "localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_model=List[schemas.Todo])
async def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)


@app.post("/", response_model=schemas.Todo)
async def make_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)
