import uvicorn
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, Path, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import json

class Todo(BaseModel):
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

async def load_todos() -> List[Todo]:    
    with open("datastore/data_file.json", "r") as read_file:
        data = json.load(read_file)
        return data

async def add_todo(todo) -> str:      
    with open("datastore/data_file.json", "r+") as write_file:
        file_data = json.load(write_file)
        file_data.append(todo)
        write_file.seek(0)
        json.dump(file_data, write_file, indent = 4)

async def validate_id(str):
    try:
        int(str)
    except ValueError:
        detail = f"Non-integer value was provided"
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail=detail)
    
@app.get('/',name='home')
async def index():
    return {"message": "Welcome home"}

@app.post('/todo', name='Create a todo', status_code=status.HTTP_201_CREATED)
async def todos_post(req: Request):
    __todos = await load_todos()
    reqTodo = await req.json()
    id = reqTodo["id"]
    await validate_id(id)
        
    result = [todo for todo in __todos if todo["id"] == id]    
    if result:        
        detail = f"Resource with id: {id} already exists"
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=detail)
    
    await add_todo(reqTodo)
    
    return {
        "status" : "SUCCESS",
        "data" : reqTodo
    }

@app.get("/todo/{item_id}", status_code=status.HTTP_200_OK, name='Get a todo', response_model=Todo)
async def fetch_todo(item_id: int = Path(..., title="The ID of the item to get")):
    __todos = await load_todos()
    
    result = [todo for todo in __todos if todo["id"] == item_id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.get('/todos', name='Get all todos', status_code=status.HTTP_200_OK,  response_model=List[Todo])
async def todos_get() -> List[Todo]:
    __todos = await load_todos()
    return  __todos
        

if __name__ == '__main__':    
    # run the application container
    print("Running on port 8000")
    uvicorn.run(app=app, port=8000, host='localhost')