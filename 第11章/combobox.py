from tkinter import *  
from tkinter import ttk  

def show_msg(*args):  
    print(color_select.get())  
  
root=Tk()  
name=StringVar()  
color_select= ttk.Combobox(root, textvariable=name)  
color_select["values"]= ("red", "green", "blue")  
color_select["state"] = "readonly"  
color_select.current(0)  
color_select.bind("<<ComboboxSelected>>", show_msg)  
color_select.pack()  
root.mainloop()  
