import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "https://v2.jokeapi.dev/joke/"
categories = ["Programming", "Misc", "Pun", "Spooky", "Christmas"]

def get_joke():
    category = category_combo.get()
    joke_label.config(text="Loading... 🤔")
    root.update()

    try:
        response = requests.get(f"{API_URL}{category}?type=single,twopart")
        data = response.json()

        if data['type'] == 'single':
            joke = data['joke']
        else: 
            joke = f"{data['setup']}\n\n{data['delivery']}"

        joke_label.config(text=joke)

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "No internet")
    except:
        messagebox.showerror("Error", "Joke load nahi hua 😅")

root = tk.Tk()
root.title("Day 34 - Joke Generator")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="😂 Joke Generator 😂", font=("Arial", 18, "bold")).pack(pady=10)

# Category select
tk.Label(root, text="Choose Category:", font=("Arial", 12)).pack()
category_combo = ttk.Combobox(root, values=categories, state="readonly", font=("Arial", 11))
category_combo.set("Programming") 
category_combo.pack(pady=5)

tk.Button(root, text="Naya Joke Lao", command=get_joke, bg="#FF5722", fg="white",
          font=("Arial", 13, "bold"), width=15).pack(pady=15)

joke_label = tk.Label(root, text="Button dabao aur haso", 
                      font=("Arial", 12), fg="#333", wraplength=350, justify="center")
joke_label.pack(pady=20, padx=10)

root.mainloop()
