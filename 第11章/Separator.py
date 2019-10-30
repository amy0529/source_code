import tkinter as tk
from tkinter import ttk
class LSeparator(tk.Frame):
    def __init__(self,parent,text="",width=""):
        tk.Frame.__init__(self,parent)
        self.separator=ttk.Separator(self,orient=tk.HORIZONTAL)
        self.separator.grid(row=0,column=0,sticky="ew")
        self.label=ttk.Label(self,text=text)
        self.label.grid(row=0,column=0,padx=width)
       
if __name__=="__main__":
    root=tk.Tk ()
    root.geometry ("150x100")
    label=LSeparator(root,text="菜单",width=15)
    label.grid(sticky="ew")
    root.mainloop ()
