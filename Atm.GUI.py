import tkinter as tk
from tkinter import messagebox
balance=10000
def show_balance():
	global balance
	messagebox.showinfo("Balance",f"Current Balance=Rs{balance}")
	
def debit_balance():
	global balance
	a=int(amount_textbox.get())
		try:
			if(a>balance):
			 messagebox.showinfo("Insufficient balance")
			 elif(a<=0):
			 	messagebox.showerror("please enter a valid value")
			 	else:
			 		balance=balance-a
			 		messagebox.showinfo("success",  "successfullydebited")
		except ValueError:
			messagebox.showerror("Error","Enter valid value")
	 	
def credit_balance():
	global balance
	a=int(amount_textbox.get())
	balance=balance+a
	messagebox.showinfo("success", "successfully credited")
	
root=tk.Tk()
root.geometry("300x400")
root.configure(bg="#00FF00")
amount_label= tk.Label(root,text="Enter amount")
amount_label.pack(pady=20)
amount_textbox= tk.Entry(root)
amount_textbox.pack(pady=20)
credit_button= tk.Button(root,text="credit",command=credit_balance)
credit_button.pack(pady=5)
debit_button= tk.Button(root,text="debit",command=debit_balance)
debit_button.pack(pady=5)
show_button= tk.Button(root,text="show",command=show_balance)
show_button.pack(pady=5)
root.mainloop()
