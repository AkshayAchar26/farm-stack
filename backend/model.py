from pydantic import BaseModel
# from uuid import UUID,uuid1




class Todo(BaseModel):
    # id : UUID = uuid1
    title : str
    description : str