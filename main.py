from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

JOJOapp = FastAPI()

@JOJOapp.get('/blog')
def index(limit =99,pb: bool = 'true', sort: Optional[str] = None):
    if pb:
        return {'data': f'{limit} pb blogs list from the db'}
    else:
        return {'data': f'{limit} unpb blogs list from the db'}


@JOJOapp.get('/blog/unpublished')
def unpublish():
    #fetch bloh with id = id
    return{'data': 'all unpublish blogs'}

@JOJOapp.get('/blog/{id}')
def show(id: int):
    #fetch bloh with id = id
    return{'data': id}


@JOJOapp.get('/blog/{id}/comments')
def about(id,limit = 10):
    #fetch bloh with id = id
    return{'data':{'4','9','7'}}


class Blog(BaseModel):
    title: str
    body:str
    published_at:Optional[bool]


@JOJOapp.post('/blog')
def create_blog(JOJO_re:Blog):
    return{'data': f"Blog is created with title as {JOJO_re.title}"}

