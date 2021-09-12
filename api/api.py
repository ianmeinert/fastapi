import uvicorn
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
import json

class todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool
    
app= FastAPI()

origins = [
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET','POST'],
    allow_headers=["*"],
)

__todos: List[todo] = None

async def load_todos() -> List[todo]:    
    with open("datastore/data_file.json", "r") as read_file:
        data = json.load(read_file)
        return data

async def add_todo(todo:todo) -> str:
    __todos.append({
        "userId": todo.userId,
        "id": todo.id,
        "completed": todo.completed,
        "title": todo.title
    })
    
    return 'todo added'    
    
@app.get('/',name='home')
async def index():
    return {"message": "Welcome home"}

@app.post('/todo', name='Create a todo', response_model=todo)
async def todos_post(todo: todo) -> todo:
    await add_todo(todo = todo)
    return todo

@app.get("/todo/{item_id}", status_code=200, name='Get a todo', response_model=todo)
async def fetch_todo(item_id: int = Path(..., title="The ID of the item to get")):
    __todos = await load_todos()
    result = [todo for todo in __todos if todo["id"] == item_id]
    if result:
        return result[0]

@app.get('/todos', name='Get all todos', response_model=List[todo])
async def todos_get() -> List[todo]:
    __todos = await load_todos()
    return  __todos
        

if __name__ == '__main__':    
    # run the application container
    print("Running on port 8000")
    uvicorn.run(app=app, port=8000, host='localhost')