import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILE_NAME = "tasks.json"

root = tk.Tk()
root.title("Day 30 - To-Do List")
root.geometry("400x500")

tasks = [] # saare kaam yaha list me rahenge

def load_tasks():
    global tasks
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = json.load(f)
    refresh_list()

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def refresh_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "○"
        listbox.insert(tk.END, f"{status} {task['text']}")

def add_task():
    task_text = simpledialog.askstring("Add Task", "Naya kaam likho:")
    if task_text:
        tasks.append({"text": task_text, "done": False})
        save_tasks()
        refresh_list()

def toggle_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks()
        refresh_list()
    except:
        messagebox.showwarning("Error", "Pehle koi task select karo")

def delete_task():
    try:
        index = listbox.curselection()[0]
        del tasks[index]
        save_tasks()
        refresh_list()
    except:
        messagebox.showwarning("Error", "Pehle koi task select karo")

# UI
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=15, font=("Arial", 12))
listbox.pack(side=tk.LEFT)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.LEFT, fill=tk.Y)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_task, width=10, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Done/Undo", command=toggle_done, width=10, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_task, width=10, bg="#f44336", fg="white").grid(row=0, column=2, padx=5)

load_tasks() # shuru me purane task load karo
root.mainloop()
