from pydantic import BaseModel

class TaskIn(BaseModel):
    title: str

class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool