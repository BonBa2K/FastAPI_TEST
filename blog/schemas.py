from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class ShowBlog(BaseModel):
    title: str
    body: str
    id: int
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password:str

class ShowUser(BaseModel):
    name: str
    email: str
    id:int
    class Config():
        orm_mode = True 