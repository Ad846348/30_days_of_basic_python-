import tkinter as tk
from tkinter import messagebox

tasks = []

def show_task():
    task_listbox.delete(0, tk.END) # listbox clear
    if len(tasks) == 0:
        messagebox.showinfo("Your tasks", "No task available")
    else:
        for i, task in enumerate(tasks, 1):
            task_listbox.insert(tk.END, f"{i}. {task}") # listbox me add

def add_task():
    a = task_entry.get().strip()
    if a == "":
        messagebox.showerror("Error", "Add some task")
        return
    tasks.append(a)
    task_entry.delete(0, tk.END)
    show_task()
    messagebox.showinfo("Success", "Task added")

def delete_task():
    if len(tasks) == 0:
        messagebox.showinfo("Info", "No Task to delete")
        return
    try:
        b = int(del_entry.get())
        if 1 <= b <= len(tasks): 
            removed = tasks.pop(b-1)
            del_entry.delete(0, tk.END)
            show_task()
            messagebox.showinfo("Success", f"Deleted: {removed}")
        else:
            messagebox.showinfo("Sorry", "Task not found")
    except ValueError:
        messagebox.showerror("Error", "Enter only numbers!")

root = tk.Tk()
root.title("To_do_list")
root.geometry("300x400")
root.configure(bg="#E7E84F")

task_label = tk.Label(root, text="Enter your task", bg="#E7E84F")
task_label.pack(padx=10, pady=10)
task_entry = tk.Entry(root, width=30)
task_entry.pack(padx=10, pady=10)

add_button = tk.Button(root, text="Add", command=add_task, width=20)
add_button.pack(pady=5)

tk.Label(root, text="Tasks:", bg="#E7E84F").pack()
task_listbox = tk.Listbox(root, width=40) # yahi dikhayega task
task_listbox.pack(pady=10)

del_label = tk.Label(root, text="Enter task number to delete", bg="#E7E84F")
del_label.pack(padx=10, pady=5)
del_entry = tk.Entry(root, width=10)
del_entry.pack(padx=10, pady=5)

show_button = tk.Button(root, text="Show", command=show_task, width=20)
show_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete", command=delete_task, width=20)
delete_button.pack(pady=5)

root.mainloop()