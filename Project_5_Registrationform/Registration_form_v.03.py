import tkinter as tk
from tkinter import messagebox

def submit_data():
    name = name_textbox.get()
    dob = DOB_textbox.get()
    gender = Gender_textbox.get()
    email = Email_textbox.get()
    address = Address_textbox.get()

    if name == "" or dob == "" or gender == "" or email == "" or address == "":
        messagebox.showerror("Error", "Fill all the details")
        return

    with open("user.txt", "a") as f:
        f.write(f"Name: {name}, DOB: {dob}, Gender: {gender}, Email: {email}, Address: {address}\n")

    messagebox.showinfo("Success", "Data Saved!")
    
    
    name_textbox.delete(0, tk.END)
    DOB_textbox.delete(0, tk.END)
    Gender_textbox.delete(0, tk.END)
    Email_textbox.delete(0, tk.END)
    Address_textbox.delete(0, tk.END)


root = tk.Tk()
root.title("Student Registration Form")
root.geometry("300x350")

tk.Label(root, text="Enter name:").pack()
name_textbox = tk.Entry(root)
name_textbox.pack()

tk.Label(root, text="Enter date of birth MM/DD/YY").pack()
DOB_textbox = tk.Entry(root)
DOB_textbox.pack()

tk.Label(root, text="Enter gender").pack()
Gender_textbox = tk.Entry(root)
Gender_textbox.pack()

tk.Label(root, text="Enter email").pack()
Email_textbox = tk.Entry(root)
Email_textbox.pack()

tk.Label(root, text="Residential address").pack()
Address_textbox = tk.Entry(root)
Address_textbox.pack()

submit_button = tk.Button(root, text="Submit", command=submit_data, bg="green", fg="white")
submit_button.pack(pady=10)

root.mainloop()
