import json
import os

TASKS = "data/tasks.json"

class TasksManager:
    def save_task(self, data):
        with open(TASKS, "a") as file:
            json.dump(data, file)

    def load(self):
        with open(TASKS, "r") as file:
            json.load()