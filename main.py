"""FastAPI automation server."""
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import asyncio

app = FastAPI()

class TaskInput(BaseModel):
    name: str
    payload: dict | None = None

@app.post("/tasks")
async def create_task(task: TaskInput, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_task, task.name, task.payload or {})
    return {"task_id": task.name, "status": "queued"}

async def run_task(name: str, payload: dict):
    await asyncio.sleep(1)
    print(f"Task {name} completed with payload: {payload}")

@app.get("/health")
def health():
    return {"status": "ok"}
