from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    task: str

    class Config:
        from_attributes = True
        
class ToDoCreate(BaseModel):
    task: str    


    