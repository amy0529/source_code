from tkinter import ttk
import tkinter as tk

root=tk.Tk()
tree=ttk.Treeview(root)
tree["columns"]=("one","two")
tree.column("one", width=100 )
tree.column("two", width=100)
tree.heading("one",text="姓名")
tree.heading("two",text="年龄")
tree.insert("",0,text="班主任", values=("张老师","30"))
id2=tree.insert("",1, "dir2", text="班委")
tree.insert(id2,"end","dir3", text="班长", values=("张三","20"))
tree.insert(id2,"end","dir4", text="学委", values=("李斯","19"))
id3=tree.insert("",2,"dir5",text="同学")
tree.insert(id3,"end","dir6", text="男同学",values=("刘大","19"))
tree.insert(id3,"end","dir7", text="男同学",values=("张大","19"))
tree.insert(id3,"end","dir8", text="女同学",values=("李馨","19"))
tree.insert(id3,"end","dir9", text="女同学",values=("王香","19"))
tree.pack()
root.mainloop() 

