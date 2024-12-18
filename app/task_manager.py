import os

class TaskManager:
    def __init__(self):
        self.file_path = "data/tasks.txt"
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def clear_tasks(self):
        self.tasks = []
        self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

