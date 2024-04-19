from fastapi import FastAPI

from models import Todo

app = FastAPI()

todos: list[Todo] = []


@app.get("/")
async def get_todos() -> list[Todo]:
    return todos


@app.post("/")
async def create_todo(todo: Todo) -> None:
    todos.append(todo)
