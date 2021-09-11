import uvicorn
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware

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

class Chore(BaseModel):
    id: int
    name: str
    days_until_alert: int
    date_added: Optional[str]

__todo: List[Chore] = [
    {
        "id": "1",
        "name": "walk dog",
        "days_until_alert": 1,
        "date_added": datetime.now().strftime("%Y-%m-%d")
    },
    {
        "id": "2",
        "name": "feed cats",
        "days_until_alert": 3,
        "date_added": datetime.now().strftime("%Y-%m-%d")
    }
]

async def get_todos() -> List[Chore]:
        return __todo

async def add_todo(chore:Chore) -> str:
    __todo.append({
        "id": chore.id,
        "name": chore.name,
        "days_until_alert": chore.days_until_alert,
        "date_added": datetime.now().strftime("%Y-%m-%d")
    })
    
    return 'todo added'

    
@app.get('/',name='home')
async def index():
    return {"message": "Welcome home"}

@app.post('/todo', name='Create a todo', response_model=Chore)
async def todos_post(chore: Chore) -> Chore:
    await add_todo(chore = chore)
    return chore

@app.get("/todo/{item_id}", status_code=200, name='Get a todo', response_model=Chore)
async def fetch_todo(item_id: str = Path(..., title="The ID of the item to get")):
    result = [chore for chore in __todo if chore["id"] == item_id]
    if result:
        return result[0]

@app.get('/todos', name='Get all todos', response_model=List[Chore])
async def todos_get() -> List[Chore]:
    return await get_todos()

if __name__ == '__main__':
    print("Running on port 8000")
    uvicorn.run(app=app, port=8000, host='localhost')