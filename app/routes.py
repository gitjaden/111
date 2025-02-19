from flask import Flask, request
from app.database import task


app = Flask(__name__)

# ReST=representation State Trasnder
# is an architectural desgin pattern that helps design out API (services)


@app.get("/")
@app.get("/tasks")
def get_all_tasks():
    out = {"task": task.scan(), "ok": True}
    return out


@app.get("/tasks/<int:pk>")  # path--type conversion int
def get_single_task(pk):  # primary key
    out = {"task": task.select_by_id(pk), "ok": True}
    return out


# this route should be mapped to a function that creates new tasks
@app.post("/tasks")
def create_task():  # primary key
    task_data = request.json
    task.create_task(task_data)
    return "", 201


# this routeshould be mapped to a function that deletes existing tasks
@app.delete("/tasks/<int:pk>")  # path--type conversion int
def delete_by_id(pk):  # primary key
    task.delete_by_id(pk)
    return "", 204


# this route should be ampped to a function that update existing tasks
@app.put("/tasks/<int:pk>")
def update_task(pk):
    task_data = request.json
    task.update_by_id(task_data, pk)
    return "", 204


"""
{
    "name": "task name",
    "summary": "task summary",
    "description": "task description"
}
"""
