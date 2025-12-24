from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

# Helper: Load tasks from file

def load_tasks():
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json", "r") as f:
        return json.load(f)

# Helper: Save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

# Home Page
@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

# Add Task
@app.route("/add", methods=["POST"])
def add_task():
    task_text = request.form.get("task")

    if not task_text.strip():
        return redirect("/")  # ignore empty tasks

    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "text": task_text})
    save_tasks(tasks)
    return redirect("/")

# Edit Task
@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    new_text = request.form.get("task")

    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["text"] = new_text
            break

    save_tasks(tasks)
    return redirect("/")

# Delete Task

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]

    # Reassign IDs to avoid gaps
    for idx, task in enumerate(tasks):
        task["id"] = idx + 1

    save_tasks(tasks)
    return redirect("/")

# Run app
if __name__ == "__main__":
    app.run(debug=True)
