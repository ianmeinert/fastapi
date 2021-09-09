import uvicorn
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel
import fastapi


api= fastapi.FastAPI()

class Chore(BaseModel):
    name: str
    days_until_alert: int
    date_added: Optional[str]

__todo: List[Chore] = [
    {
        "name": "walk dog",
        "days_until_alert": 1,
        "date_added": datetime.now().strftime("%Y-%m-%d")
    }
]

async def get_todos() -> List[Chore]:
        return __todo
    
@api.get('/',name='home')
async def indexs():
    return {"message": "Welcome home"}

async def add_todo(chore:Chore) -> str:
    __todo.append({
        "name": chore.name,
        "days_until_alert": chore.days_until_alert,
        "date_added": datetime.now().strftime("%Y-%m-%d")
    })
    
    return 'todo added'

@api.get('/todos', name='Get all todos', response_model=List[Chore])
async def todos_get() -> List[Chore]:
    return await get_todos()

@api.post('/todos', name='Create a todo', response_model=Chore)
async def todos_post(chore: Chore) -> Chore:
    await add_todo(chore = chore)
    return chore

if __name__ == '__main__':
    print("Running on port 8000")
    uvicorn.run(app=api, port=8000, host='127.0.0.1')