from tkinter import *  
from tkinter import ttk
root=Tk()
root.geometry("200x150")
n=ttk.Notebook(root)
f1=ttk.Frame(n,height=100,width=100)
f2=ttk.Frame(n,height=100,width=100)   
n.add(f1, text='One')
n.add(f2, text='Two')
n.pack()
root.mainloop()  
