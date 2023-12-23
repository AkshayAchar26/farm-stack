from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

#fastAPI instance as app
app = FastAPI()

origins = [
    "http://localhost:3000"
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
    return 1

@app.get('/api/todo{title}')
async def get_todo_by_ID(title : str):
    return 1

@app.post('/api/todo')
async def post_todo(todo : Todo):
    return 1

@app.put('/api/todo{title}')
async def update_todo(title : str , todo : Todo):
    return 1

@app.delete('/api/todo{title}')
async def delete_todo(title : str):
    return 1


    


