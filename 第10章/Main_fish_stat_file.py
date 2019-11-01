from module.Class_module import FishBox
import os
def save_file(file_name,L_newRecord):
    flag=False
    if type(L_newRecord)!=list:
        print("保存内容必须以列表对象格式进行!保存失败!")
        return flag
    
    cur_path=os.path.abspath(os.path.curdir) 
    cur_path=cur_path+'\\'+file_name
    try:
        f1=open(cur_path,'w')
        f1.writelines(L_newRecord)
        flag=True
    except:
        flag=False
    finally:
        if flag:
            f1.close()  
    return flag
#===============================创建大礼盒实例，并求相关值
L_SaveData=[]
big_gift_box=FishBox(60,30,40)  #创建长60cm,宽30cm，高40cm的大礼盒实例
big_gift_box.price=1000         #价格1000元
big_gift_box.amount=20          #1盒存放20条
big_gift_box.weight=10          #10公斤
#print("大礼盒的体面积是%d立方厘米"%(big_gift_box.volume()))
#print("大礼盒的表面积是%d平方厘米"%(big_gift_box.area()))
L_SaveData.append("大礼盒的体面积是"+str(big_gift_box.volume())+"立方厘米")
L_SaveData.append("大礼盒的表面积是"+str(big_gift_box.area())+"平方厘米")
index=big_gift_box.type.index('大礼盒')
g_box_num=big_gift_box.countBoxNums(200,index)
#print("200条鱼需要%d只大礼盒"%(g_box_num))
#print("200条鱼装大礼盒的价值为%d元"%(g_box_num*big_gift_box.price))
L_SaveData.append("200条鱼需要"+str(g_box_num)+"只大礼盒")
L_SaveData.append("200条鱼装大礼盒的价值为"+str(g_box_num*big_gift_box.price)+"元")
#===============================创建小礼盒实例，并求相关值
small_gift_box=FishBox(50,20,30)  #创建长50cm,宽20cm，高30cm的小礼盒实例
small_gift_box.price=500         #价格500元
small_gift_box.amount=10          #1盒存放10条
small_gift_box.weight=5          #5公斤
#print("小礼盒的体面积是%d立方厘米"%(small_gift_box.volume()))
#print("小礼盒的表面积是%d平方厘米"%(small_gift_box.area()))
L_SaveData.append("小礼盒的体面积是"+str(small_gift_box.volume())+"立方厘米")
L_SaveData.append("小礼盒的表面积是"+str(small_gift_box.area())+"平方厘米")
index=small_gift_box.type.index('小礼盒')
g_box_num=small_gift_box.countBoxNums(200,index)
#print("200条鱼需要%d只小礼盒"%(g_box_num))
#print("200条鱼装小礼盒的价值为%d元"%(g_box_num*small_gift_box.price))
L_SaveData.append("200条鱼需要"+str(g_box_num)+"只小礼盒")
L_SaveData.append("200条鱼装小礼盒的价值为"+str(g_box_num*small_gift_box.price)+"元")
if save_file('fish_records.txt',L_SaveData):
    print('三酷猫装盒子数据保存成功!')
else:
   print('三酷猫装盒子数据保存操作失败!')

