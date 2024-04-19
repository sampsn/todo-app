from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


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
async def make_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)) -> None:
    crud.create_todo(db, todo)
