import pymysql
import sys
import tkinter.messagebox
sDate= StringVar()
sname= StringVar()
snums= StringVar()
sprice= StringVar()
sExplain= StringVar()

def turn_save(event):                    #自定义回调函数turn_property
    
    #============================往表插入新记录
    try:   
        conn=pymysql.connect(host='localhost', user='root', passwd='mysql123', db='test', port=3306,
                                 charset='utf8')
    except:
        print("打开数据库连接出错，请检查！")
        conn.close()
        sys.exit()
    cur=conn.cursor()
    selectSQL="Insert into T_fish values('"+sDate+"'','"+sname+"',"+snums+","+sprice+",'"+sExplain+")"
    cur.execute(selectSQL)
    cur.close()
    conn.close()
    tkinter.messagebox.showinfo('提示','记录保存成功!')
def turn_property(event):                    #自定义回调函数turn_property
        getSQLDate()
def getSQLDate():
    #============================显示表内容
    try:   
        conn=pymysql.connect(host='localhost', user='root', passwd='mysql123', db='test', port=3306,
                                 charset='utf8')
    except:
        print("打开数据库连接出错，请检查！")
        conn.close()
        sys.exit()
    cur=conn.cursor()
    selectSQL='Select * from T_fish'
    cur.execute(selectSQL)
    for row in cur.fetchall():
        tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4])) #插入第1行记录
    cur.close()
    conn.close()
        
import tkinter.tix
import tkinter as tk
from tkinter.constants import *
from tkinter import ttk                              #导入ttk模块
from tkinter.constants import *
root=tkinter.tix.Tk()

tree=ttk.Treeview(root)                              #创建树状结构列表实例
tree["columns"]=("name","nums","price","Explain")                      #设置二个列对象名
tree.column("name", width=50)                        #设置第一个列宽度
tree.column("nums", width=50)                      #设置第二个列宽度
tree.column("price", width=50)                        #设置第一个列宽度
tree.column("Explain", width=50)                      #设置第二个列宽度
tree.heading("name",text="名称")                      #给第一个列设置标题
tree.heading("nums",text="数量")                      #给第一个列设置标题
tree.heading("price",text="单价（元）")              #给第二个列设置标题
tree.heading("Explain",text="说明")                  #给第二个列设置标题
tree.pack(side="top")
bs=tk.Button(root,text="显示数据",width=10)        #在标签框架上创建Button实例bs
bs.bind("<Button-1>",turn_property)           #bind()绑定鼠标进入事件
bs.pack(side="top")


top=tkinter.tix.Frame(root, relief=RAISED,bd=1)
top.pack(side='left')
top.date1=tkinter.tix.LabelEntry(top,label="日期:",labelside='top',variable=sDate)
top.date1.pack(side="left")
top.name1=tkinter.tix.LabelEntry(top,label="名称:",labelside='top',variable=sname)
top.name1.pack(side="left")
top.nums1=tkinter.tix.LabelEntry(top,label="数量:",labelside='top',variable=snums)
top.nums1.pack(side="left")
top.price=tkinter.tix.LabelEntry(top,label="价格:",labelside='top',variable=sprice)
top.price.pack(side="left")
top.Explain=tkinter.tix.LabelEntry(top,label="说明:",labelside='top',variable=sExplain)
top.Explain.pack(side="left")
Savebn=tk.Button(top,text="保存数据",width=10)        #在标签框架上创建Button实例bs
Savebn.bind("<Button-1>",turn_save)           #bind()绑定鼠标进入事件
Savebn.pack(side="left")
root.mainloop()
