from tkinter import tix
import tkinter
def btnDialog(w):                                     #自定义按钮对话框函数
    bbox=tix.ButtonBox(w,orientation=tix.HORIZONTAL)  #创建水平的ButtonBox实例
    bbox.add('ok',text='确认',underline=0,width=5,    #增加“确认”按钮
             command=lambda w=w: w.destroy())         #带窗体关闭功能
    bbox.add('close',text='取消',underline=0,width=5, #增加“取消”按钮
             command=lambda w=w: w.destroy())         #带窗体关闭功能
    bbox.pack(side=tix.BOTTOM, fill=tix.X)            #bbox对象在窗体上的定位
if __name__ == '__main__':                           #如果直接调用并执行该文件
    root=tix.Tk()                                    #创建窗体实例
    btnDialog(root)                                  #调用btnDialog自定义函数
    root.mainloop()                                  #启动窗体消息循环功能
