from model import Todo
import motor.motor_asyncio
from bson.binary import UuidRepresentation
from config import get_settings

settings = get_settings()
mongo_url = settings.mongo_url

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url,UuidRepresentation = 'standard')
db = client.TodoList
collection = db.todo


async def fetch_one_todo(title:str):
    document = await collection.find_one({'title': title})
    return document

async def fetch_all_todos():
    todos = []
    curser = collection.find({})
    async for document in curser:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo : Todo):
    await collection.insert_one(todo)
    return todo

async def update_todo(title:str,description:str):
    await collection.update_one({'title':title},{"$set":{'description':description}})
    result = await collection.find_one({'title':title})
    return result


async def remove_todo(title:str):
    await collection.delete_one({'title':title})
    return True