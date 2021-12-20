from typing import List,Optional
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int
    class Config():
        orm_mode = True 

class Blog(BlogBase):
    class Config():
        orm_mode = True 


class User(BaseModel):
    name: str
    email: str
    password:str

class ShowUser(BaseModel):
    name: str
    email: str
    password:str
    blogs :List[Blog]= []

    id:int
    class Config():
        orm_mode = True 
    

class ShowBlog(BaseModel):
    title: str
    body: str
    id: int
    creator: ShowUser

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None