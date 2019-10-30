import tkinter as tk
from tkinter import scrolledtext
root=tk.Tk()
root.title("滚动文本框")
root.geometry("200x100")
sWidth=10             #设置文本框的长度
sHeight=3              #设置文本框的高度
s_show=scrolledtext.ScrolledText(root,width=sWidth,height=sHeight,wrap=tk.WORD)
s_show.insert('insert',"一行10个字符")
s_show.grid(column=0,columnspan=2)
root.mainloop()      
