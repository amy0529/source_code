from multiprocessing import Process        #导入multiprocessing模块指定对象
from datetime import datetime              #导入datetime模块
def do1(j):                                #自定义打印函数（供进程调用）
    print("第%d进程！"%(j))
 
class MyProcess(Process):                   #自定义进程类MyProcess
    def __init__(self,target,args):         #定义类构造函数__init__
        Process.__init__(self)              #继承Process的构造函数
        self.target=target                  #把自定义函数传递给属性target
        self.args=args                      #把函数对应的参数传递给属性args
     def run(self):                         #重写run方法
        self.target(self.args)              #调用自定义函数
  
if __name__=='__main__':                    #主程序，执行后面的程序
    print('开始时间：',datetime.now())      #打印开始时间
    for i in range(10):                     #循环产生0到9的进程
        p1=MyProcess(target=do1,args=(i,))  #创建传递自定义函数和参数的进程
        #p1.daemon = True
        p1.start()                          #启动进程
        p1.join()                           #进程阻塞
    print('结束时间：',datetime.now())      #打印程序结束时间
