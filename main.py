from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
"""A simple Task API for managing tasks"""

class tasks(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    done: bool | None = Field(default=None, index=True)


sqlite_file_name = "tasks.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)
#SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

"""Root endpoint"""
@app.get("/")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

"""
GET /tasks - Get all tasks

"""
@app.get("/tasks")
async def get_tasks(session: SessionDep):
    return session.exec(select(tasks)).all()

"""
GET /tasks/{task_id} - Get a specific task by ID
"""
@app.get("/tasks/{task_id}")
async def get_task(session: SessionDep, task_id: int):
    task = session.get(tasks, task_id)
    if task:
        return task
    return {"error": f"Task {task_id} not found"}

"""
POST /tasks - Create a new task
"""
@app.post("/tasks")
async def create_task(task: tasks, session: SessionDep) ->tasks:
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

"""
PUT /tasks/{task_id} - Update an existing task by ID
"""
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: dict):
    if task_id in tasks:
        tasks[task_id] = task
        return {"id": task_id, "task": task}
    return {"error": f"Task {task_id} not found"}

"""
DELETE /tasks/{task_id} - Delete a specific task by ID
"""
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int, session: SessionDep):
    task = session.get(tasks, task_id)
    if task:
        session.delete(task)
        session.commit()
        return {"message": f"Task {task_id} deleted"}
    return {"error": f"Task {task_id} not found"}


"""
Health check endpoint
"""
@app.get("/health")
async def health():
    return {"status": "ok"}