from tkinter import *  
from tkinter import ttk  
  
root=Tk()  
ttk.Sizegrip(root).grid(row=59,column=59,sticky="se")  
root.columnconfigure(0,weight=1,minsize=59)  
root.rowconfigure(0,weight=1,minsize=59)  
root.mainloop() 
