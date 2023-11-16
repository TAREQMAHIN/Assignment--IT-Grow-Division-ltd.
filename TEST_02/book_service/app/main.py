# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Author, Book, Client
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ... Implement CRUD operations for books, authors, and clients using FastAPI

@app.get("/books/")
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


## Implement Bearer Token Authentication in FastAPI. Useing OAuth2 for simplicity.

@app.get("/secure-books/")
def get_secure_books(token: str = Depends(security), db: Session = Depends(get_db)):

    books = db.query(Book).all()
    return books