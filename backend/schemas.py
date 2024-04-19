from pydantic import BaseModel


class TodoBase(BaseModel):
    number: int
    description: str


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True
