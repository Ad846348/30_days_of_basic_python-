import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Day 29 - Calculator")
root.geometry("320x450")
root.resizable(False, False)

expression = "" # jo bhi type hoga yaha store hoga

# Display box
input_text = tk.StringVar()

def press(num):
    global expression
    expression = expression + str(num)
    input_text.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression)) # expression ko calculate karega
        input_text.set(total)
        expression = total
    except:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

# Display
display = tk.Entry(root, textvariable=input_text, font=("Arial", 20), bd=10, justify="right")
display.pack(fill=tk.BOTH, padx=10, pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ['C', '⌫', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == '=':
            btn = tk.Button(btn_frame, text=btn_text, width=15, height=2, command=equalpress, bg="#4CAF50", fg="white", font=("Arial", 14))
        elif btn_text == 'C':
            btn = tk.Button(btn_frame, text=btn_text, width=7, height=2, command=clear, bg="#f44336", fg="white", font=("Arial", 14))
        elif btn_text == '⌫':
            btn = tk.Button(btn_frame, text=btn_text, width=7, height=2, command=backspace, bg="#ff9800", fg="white", font=("Arial", 14))
        else:
            btn = tk.Button(btn_frame, text=btn_text, width=7, height=2, command=lambda x=btn_text: press(x), font=("Arial", 14))
        btn.grid(row=i, column=j, padx=2, pady=2)

root.mainloop()
