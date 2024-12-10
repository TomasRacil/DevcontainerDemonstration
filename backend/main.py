#!/usr/local/bin/python

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel
from os import getenv
import uvicorn

# Database configuration
# Replace with your actual database credentials
db_password = getenv("POSTGRES_PASSWORD", "postgres")
# db_password = environ["POSTGRES_PASSWORD"]
db_name = getenv("POSTGRES_DB", "postgres")
# db_name = environ["POSTGRES_DB"]
db_user = getenv("POSTGRES_USER", "postgres")
# db_user = environ["POSTGRES_USER"]
db_host = "db"
db_port = "5432"
DATABASE_URL = f"postgresql://{db_user}:{
    db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Define the Todo model
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)


# Create the table if it doesn't exist
Base.metadata.create_all(bind=engine)


# Pydantic models for request and response
class TodoCreate(BaseModel):
    task: str


class TodoRead(BaseModel):
    id: int
    task: str


# Dependency to get a database session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create the FastAPI app
app = FastAPI()

# API endpoints


@app.get("/")
def home_todo():
    return "Ukazkova todo stranka"


@app.post("/todos/", response_model=TodoRead)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(task=todo.task)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


@app.get("/todos/", response_model=list[TodoRead])
def read_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()


@app.get("/todos/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
