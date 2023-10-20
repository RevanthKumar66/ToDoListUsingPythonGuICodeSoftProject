import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.tasks = []
        # Create widgets
        self.title_label = tk.Label(master, text="To-Do List", font=("Arial", 20))
        self.task_label = tk.Label(master, text="Enter task:", font=("Arial", 14))
        self.task_entry = tk.Entry(master, width=40)
        self.add_button = tk.Button(master, text="Add task", command=self.add_task)
        self.tasks_listbox = tk.Listbox(master, width=40)
        self.remove_button = tk.Button(master, text="Remove task", command=self.remove_task)
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)

        # Grid widgets
        self.title_label.grid(row=0, column=1)
        self.task_label.grid(row=1, column=0)
        self.task_entry.grid(row=1, column=1)
        self.add_button.grid(row=1, column=2)
        self.tasks_listbox.grid(row=2, column=0, columnspan=3)
        self.remove_button.grid(row=3, column=0)
        self.quit_button.grid(row=3, column=2)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.tasks_listbox.insert(tk.END, task)

    def remove_task(self):
        selected_task = self.tasks_listbox.curselection()
        if selected_task:
            self.tasks.remove(self.tasks_listbox.get(selected_task))
            self.tasks_listbox.delete(selected_task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()
