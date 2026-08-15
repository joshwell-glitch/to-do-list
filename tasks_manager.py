from tkinter import messagebox
import json
import os

TASKS = "data/tasks.json"

class TasksManager:
    def save_task(self, data):
        try:
            os.mkdir('data')
        except FileExistsError:
            pass
        with open(TASKS, "a") as file:
            json.dump(data, file)

    def load_task(self):
        try:
            with open(TASKS, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            pass