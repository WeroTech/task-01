from fastapi import FastAPI
"""A simple Task API for managing tasks"""

tasks = {1: {"Title": "Read a book", "done": True},
         2: {"Title": "Write a blog post", "done": False},
         3: {"Title": "Go for a walk", "done": True}}

app = FastAPI()

"""Root endpoint"""
@app.get("/")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

"""
GET /tasks - Get all tasks

"""
@app.get("/tasks")
async def get_tasks():
    return list(tasks.values())

"""
GET /tasks/{task_id} - Get a specific task by ID
"""
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = tasks.get(task_id)
    if task:
        return task
    return {"error": f"Task {task_id} not found"}

"""
POST /tasks - Create a new task
"""
@app.post("/tasks")
async def create_task(task: dict):
    task_id = max(tasks.keys()) + 1
    tasks[task_id] = task
    return {"id": task_id, "task": task}

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
async def delete_task(task_id: int):
    if task_id in tasks:
        del tasks[task_id]
        return {"message": f"Task {task_id} deleted"}
    return {"error": f"Task {task_id} not found"}


"""
Health check endpoint
"""
@app.get("/health")
async def health():
    return {"status": "ok"}