import tkinter as tk
from tkinter import messagebox
from app.task_manager import TaskManager


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        self.task_manager = TaskManager()

        # Frame for task input
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        add_button = tk.Button(input_frame, text="Add Task", font=("Arial", 12), command=self.add_task)
        add_button.pack(side=tk.LEFT)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(self.root, width=40, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Buttons for actions
        action_frame = tk.Frame(self.root)
        action_frame.pack(pady=10)

        delete_button = tk.Button(action_frame, text="Delete Task", font=("Arial", 12), command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=5)

        clear_button = tk.Button(action_frame, text="Clear All", font=("Arial", 12), command=self.clear_tasks)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Load tasks
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_manager.add_task(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.delete_task(selected_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected!")

    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.task_manager.clear_tasks()
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        self.task_manager.load_tasks()
        self.update_task_listbox()
