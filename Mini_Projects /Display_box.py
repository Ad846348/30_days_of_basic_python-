import tkinter as tk
from tkinter import scrolledtext
root=tk.Tk()
app= tk.Label(root, text="Scrolled text",font=('Georgia',44))
app.pack(fill=tk.BOTH,expand=True)
text_scroll_1=scrolledtext.ScrolledText(root,wrap=tk.WORD,height=30,bg="#B8255F"state=tk.DISABLED)
text_scroll_1.pack()
text_scroll=scrolledtext.ScrolledText(root,wrap=tk.WORD,height=30)
text_scroll.pack()
root.mainloop()

