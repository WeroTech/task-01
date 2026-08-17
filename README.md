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

## curl -i sample output

```bash
curl -i http://127.0.0.1:8000/health
```

```http
HTTP/1.1 200 OK
date: Mon, 17 Aug 2026 17:14:59 GMT
server: uvicorn
content-length: 15
content-type: application/json

{"status":"ok"}
```
