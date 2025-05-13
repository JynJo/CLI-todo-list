import json
import os 

TASK_FILE = 'db.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(task):
    with open(TASK_FILE, 'w') as file:
        json.dump(task, file, indent=4)

def list_task():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['task']} - {status}")

def clear_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    tasks.clear()
    save_tasks(tasks)    

def done_task(index):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index - 1]["completed"] = True
    save_tasks(tasks)
    print(f"Task {index} marked as completed.")

def delete_task(index):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"Task {index} deleted.")