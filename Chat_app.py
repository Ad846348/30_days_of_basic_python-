import tkinter as tk
from tkinter import scrolledtext
root=tk.Tk()
root.title("My chat app")
root.geometry("300x400")
app_header= tk.Label(root,text="My Chat Interface",bg="Dark Blue",fg="White",font= ("Georgia",24))
app_header.pack(fill=tk.X,expand=True)
Display_Text=scrolledtext.ScrolledText(root,state=tk.
DISABLED,wrap=tk.WORD,height=30)
Display_Text.pack()
Input_text=scrolledtext.ScrolledText(root,wrap=tk.WORD,height=3)
Input_text.pack()
def send_text():
	user_input=(Input_text.get("1.0",tk.END))
	Display_Text.config(state=tk.NORMAL)
	Display_Text.insert(tk.END,"You:"+user_input)
	Display_Text.insert(tk.END,"BOT:"+"I am fine,thanks!"+"\n")
	Display_Text.config(state=tk.DISABLED)
	Input_text.delete("1.0",tk.END)
send_button= tk.Button(root,text="Send",command=send_text)
send_button.pack(fill=tk.X,expand=True)
root.mainloop()
