from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from config import get_settings
from database import (
    fetch_all_todos,
    fetch_one_todo,
    create_todo,
    update_todo,
    remove_todo
)



#fastAPI instance as app
app = FastAPI()


settings = get_settings()


origins = [
    settings.origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


#
@app.get('/')
def read_root():
    return {'message':'Working!'}


@app.get('/api/todo')
async def get_todos():
    response = await fetch_all_todos()
    return response


@app.get('/api/todo{title}',response_model=Todo)
async def get_todo_by_ID(title : str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404,f'There is no todo item in this title {title}')


@app.post('/api/todo',response_model=Todo)
async def post_todo(todo : Todo):
    response = await create_todo(dict(todo))
    if response:
        return response
    raise HTTPException(400,'Somthing went worng!')


@app.put('/api/todo/{title}',response_model=Todo)
async def update_todo(title : str , description : str):
    response = await update_todo(title,description)
    if response:
        return response
    raise HTTPException(404,f'There is no todo item in this title {title}')


@app.delete('/api/todo/{title}')
async def delete_todo(title : str):
    response = await remove_todo(title)
    if response:
        return response
    raise HTTPException(404,f'There is no todo item in this title {title}')


    


