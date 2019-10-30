from tkinter import *
import tkinter.messagebox
root=Tk()

class Example(Frame):          #继承Frame组件基础上
    def __init__(self):
        super().__init__()            
        self.initUI()       
        
    def initUI(self):
        self.master.title("演示鼠标右键跳出菜单")
        self.menu=Menu(self.master, tearoff=0)
        self.menu.add_command(label="提示", command=self.showClick)
        self.menu.add_command(label="退出", command=self.onExit)
        self.master.bind("<Button-3>", self.showMenu)#鼠标右键事件,调showMenu回调函数
        self.pack()
        
    def showMenu(self, e):   #定义回调函数
        self.menu.post(e.x_root, e.y_root)
    def showClick(self):
        tkinter.messagebox.showinfo('提示','鼠标点上了!')
    def onExit(self):
        self.quit()

root.geometry("250x150")
app=Example()
root.mainloop()
