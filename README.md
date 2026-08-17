# Flyrank Task 01 - Task API

This is a simple FastAPI CRUD service for managing tasks in memory.

## Install & run

```bash
uv run fastapi dev main.py
```

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Service info |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{task_id}` | Get one task by ID |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Update a task by ID |
| DELETE | `/tasks/{task_id}` | Delete a task by ID |
| GET | `/health` | Health check |
