import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/INR" 

currencies = ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CNY"]

def convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_combo.get()
        to_curr = to_combo.get()

        if from_curr == to_curr:
            result_label.config(text="Dono same currency hai 😅")
            return

        result_label.config(text="Loading...") 
        root.update()

        response = requests.get(API_URL)
        data = response.json()
        rates = data['rates']

        
        inr_amount = amount / rates[from_curr]
        converted = inr_amount * rates[to_curr]

        result = f"{amount} {from_curr} = {converted:.2f} {to_curr}"
        result_label.config(text=result)
        
    except ValueError:
        messagebox.showerror("Error", "Sahi amount daalo. Sirf number")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Internet nahi chal raha")
    except:
        messagebox.showerror("Error", "Kuch galat ho gaya")

root = tk.Tk()
root.title("Day 33 - Currency Converter")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Live Currency Converter", font=("Arial", 16, "bold")).pack(pady=10)

# Amount
tk.Label(root, text="Amount:", font=("Arial", 12)).pack()
amount_entry = tk.Entry(root, font=("Arial", 12), width=20)
amount_entry.pack(pady=5)

# From Currency
tk.Label(root, text="From:", font=("Arial", 12)).pack()
from_combo = ttk.Combobox(root, values=currencies, state="readonly", font=("Arial", 11))
from_combo.set("USD") # default value
from_combo.pack(pady=5)

# To Currency  
tk.Label(root, text="To:", font=("Arial", 12)).pack()
to_combo = ttk.Combobox(root, values=currencies, state="readonly", font=("Arial", 11))
to_combo.set("INR") # default value
to_combo.pack(pady=5)

tk.Button(root, text="Convert", command=convert, bg="#4CAF50", fg="white",
          font=("Arial", 12, "bold"), width=15).pack(pady=15)

result_label = tk.Label(root, text="Amount daalke Convert dabao", 
                        font=("Arial", 12), fg="#333", wraplength=300)
result_label.pack(pady=10)

root.mainloop()
