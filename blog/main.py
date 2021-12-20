from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas,models,hashing
from .database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from .hashing import Hash
from .routers import blog,user,authentication

blogapp =FastAPI()

models.Base.metadata.create_all(engine)

blogapp.include_router(authentication.router)
blogapp.include_router(blog.router)
blogapp.include_router(user.router)

# def get_db():
#     db =SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()