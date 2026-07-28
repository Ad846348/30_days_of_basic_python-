import tkinter
from tkinter import messagebox
import os

balance = 10000

def load_data():
    global balance
    try:
        if os.path.exists("Data.txt"):
            f = open("Data.txt", "r")
            data = f.read()
            f.close()
            if data != "":
                balance = int(data)
    except:
        balance = 10000

def save_data():
    try:
        f = open("Data.txt", "w")
        f.write(str(balance))
        f.close()
    except:
        pass

def show_data():
    messagebox.showinfo("Balance", f"Current balance = {balance}")

def debit_data():
    global balance
    try:
        a = int(amount_entry.get())
        if a > balance:
            messagebox.showinfo("Sorry", "Insufficient balance")
        elif a <= 0:
            messagebox.showinfo("Error", "Enter valid value")
        else:
            balance = balance - a
            save_data()
            messagebox.showinfo("Success", f"Debited successfully\nNew Balance: {balance}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid value")

def credit_data():
    global balance
    try:
        a = int(amount_entry.get())
        if a > 0:
            balance = balance + a
            save_data()
            messagebox.showinfo("Success", f"Credited successfully\nNew Balance: {balance}")
        else:
            messagebox.showinfo("Error", "Enter some amount")
    except ValueError:
        messagebox.showerror("Error", "Enter valid data")

root = tkinter.Tk()
root.title("ATM Machine")
root.geometry("300x400")
root.configure(bg="#E7E84F")

load_data() # yaha load ho raha hai

tkinter.Label(root, text="Enter amount", bg="#E7E84F").pack(pady=10)
amount_entry = tkinter.Entry(root)
amount_entry.pack(pady=5)

tkinter.Button(root, text="Show", command=show_data, width=15).pack(pady=5)
tkinter.Button(root, text="Credit", command=credit_data, width=15).pack(pady=5)
tkinter.Button(root, text="Debit", command=debit_data, width=15).pack(pady=5)

root.mainloop()
