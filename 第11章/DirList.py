import tkinter.tix
from tkinter.constants import *
root=tkinter.tix.Tk()
top=tkinter.tix.Frame(root,relief=RAISED, bd=1)
top.pack(side="left")
top.dir = tkinter.tix.DirList(top)
top.dir.hlist['width'] = 40
top.dir.pack(side="left")
top.btn=tkinter.tix.Button(top,text=">> ", pady = 0)
top.btn.pack(side="left")
top.ent=tkinter.tix.LabelEntry(top, label="Installation Directory:",
                                   labelside = 'top')
top.ent.pack(side="left")
root.mainloop()




