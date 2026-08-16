from tkinter import messagebox
import json
import os

TASKS = "data/tasks.json"

class TasksManager:
    def save_task(self, task):
        try:
            with open(TASKS, "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []

        tasks.append(task)

        os.makedirs("data", exist_ok=True)

        with open(TASKS, "w") as file:
            json.dump(tasks, file, indent=4)

    def load_task(self):
        try:
            with open(TASKS, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def update_tasks(self, tasks):
        os.makedirs ("data", exist_ok=True)

        with open(TASKS, "w") as file:
            json.dump(tasks, file, indent=4)