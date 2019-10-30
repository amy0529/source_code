def turn_property(event):                    #自定义回调函数turn_property
    getSQLDate()
def getSQLDate():
    import pymysql
    import sys
    #============================连接数据库
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

import os
from tkinter import ttk                              #导入ttk模块
import tkinter as tk                                 #导入tkinter模块
root=tk.Tk()                                         #创建窗体实例
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
root.mainloop()                            #启动窗体消息循环功能


    
    
