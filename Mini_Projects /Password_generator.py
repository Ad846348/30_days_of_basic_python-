import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password():
    length = length_scale.get()
    
    characters = ""
    if var_upper.get(): characters += string.ascii_uppercase
    if var_lower.get(): characters += string.ascii_lowercase
    if var_digits.get(): characters += string.digits
    if var_symbols.get(): characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Kuch to select karo bhai!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied!", "Password copy ho gaya ✅")

root = tk.Tk()
root.title("Day 36 - Password Generator")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="🔒 Password Generator 🔒", font=("Arial", 18, "bold")).pack(pady=10)


tk.Label(root, text="Length:", font=("Arial", 11)).pack()
length_scale = tk.Scale(root, from_=4, to=32, orient="horizontal", length=250)
length_scale.set(12)
length_scale.pack()


var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="A-Z Uppercase", variable=var_upper).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="a-z Lowercase", variable=var_lower).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="0-9 Digits", variable=var_digits).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="@#$ Symbols", variable=var_symbols).pack(anchor="w", padx=80)


tk.Button(root, text="Generate Password", command=generate_password, 
          bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=10)


password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)

tk.Button(root, text="Copy", command=copy_password, 
          bg="#2196F3", fg="white", font=("Arial", 10)).pack()

root.mainloop()
