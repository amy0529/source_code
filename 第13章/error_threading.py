import threading
from time import *
from datetime import datetime
import random
tickets=[['2018-4-7 8:00','北京','沈阳',10,120],
         ['2018-4-7 9:00','上海','宁波',5,100],
         ['2018-4-7 12:00','天津','北京',20,55],
         ['2018-4-7 14:00','广州','武汉',0,200],
         ['2018-4-7 16:00','重庆','西安',3,180],
         ['2018-4-7 18:00','深圳','上海',49,780],
         ['2018-4-7 18:10','武汉','长沙',10,210],
         
         ['2018-4-8 8:00','北京','沈阳',10,120],
         ['2018-4-8 9:00','上海','宁波',5,100],
         ['2018-4-8 12:00','天津','北京',20,55],
         ['2018-4-8 14:00','广州','武汉',0,200],
         ['2018-4-8 16:00','重庆','西安',3,180],
         ['2018-4-8 18:00','深圳','上海',49,780],
         ['2018-4-8 18:10','武汉','长沙',10,210],
         
         ['2018-4-9 8:00','北京','沈阳',10,120],
         ['2018-4-9 9:00','上海','宁波',5,100],
         ['2018-4-9 12:00','天津','北京',20,55],
         ['2018-4-9 14:00','广州','武汉',0,200],
         ['2018-4-9 16:00','重庆','西安',3,180],
         ['2018-4-9 18:00','深圳','上海',49,780],
         ['2018-4-9 18:10','武汉','长沙',10,210]]
def update_prcie(start_station,nums):
    j=0
    while j<len(tickets):
        tickets[j][3]=tickets[j][3]+nums
        j+=1
    

def buy_ticket(name,nums,data1,start_station):
    i=0
    f=random()
    ss=
    sleep(0.5)
    for get_record in tickets:
        if get_record[0]==data1 and get_record[1]==start_station :
            if get_record[3]>=nums:
                tickets[i][3]=get_record[3]-nums
                print('%s购买%d张票成功！\n'%(name,nums))
                return
            else:
                print('%s现存票数量不够，无法购买！\n'%(name))
                return -1
        i+=1
    print("%s今日无票，无法购买！\n"%(name))
    return -1
class MThread(threading.Thread):
    def __init__(self,target,args):
       threading.Thread.__init__(self)
       self.target=target
       self.args=args
       
       
    def run(self):
        self.target(*self.args)
        

if __name__=='__main__':
    visitor=[('张山',3,'2018-4-9 9:00','上海'),
             ('刘六',5,'2018-4-9 9:00','上海'),
            ('李四',1,'2018-4-9 14:00','广州'),
            ('王五',2,'2018-4-9 9:00','上海'),
             ('John',2,'2018-4-9 9:00','上海'),
             ('Tom',2,'2018-4-9 9:00','上海'),
             ('Bit',2,'2018-4-9 9:00','上海'),
             ('Jack',2,'2018-4-9 9:00','上海'),
             ('Tim',2,'2018-4-9 9:00','上海')]
    class_do_list=[]
    print('开始时间：',datetime.now())
    for get_r in visitor:
        get_one=MThread(target=buy_ticket,args=get_r)
        class_do_list.append(get_one)
    get_next=MThread(target=update_prcie,args=("上海",5))    
    class_do_list.append(get_next)

    for i in range(len(class_do_list)):
        class_do_list[i].start()
    for i in range(len(class_do_list)):
        class_do_list[i].join()           
    
    print('结束时间：',datetime.now())
    print('剩余票数为：\n')
    for gets in tickets:
        print(gets)
