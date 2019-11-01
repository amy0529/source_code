from module.Class_module import FishBox
import os
import sys
sys.path[0]=r'X:\github\source_code\amy_test\module'
print(sys.path)
def save_file(file_name,L_newRecord):
    flag=False
    if type(L_newRecord)!=list:
        print(保持内容必须为列表格式,保存失败)
        return flag
    # if flag==False:
    #     print('False')
    # elif flag==True:
    #     print('Ture')
    cur_path=os.path.abspath(os.path.curdir)
    cur_path=cur_path+'\\'+file_name
    print(cur_path)
    try:
        f1=open(cur_path,'a')
        for get_L_newRecord in L_newRecord:
            f1.write(get_L_newRecord+'\n')
        # f1.writelines(L_newRecord)
        flag=True
    except:
        flag=False
    finally:
        if flag:
            f1.close()
    return flag

L_SaveData=[]
big_gift_box=FishBox(60,30,40)  #创建长60cm,宽30cm，高40cm的大礼盒实例
big_gift_box.price=1000         #价格1000元
big_gift_box.amount=20          #1盒存放20条
big_gift_box.weight=10          #10公斤
L_SaveData.append('大礼盒的体积是:'+str(big_gift_box.volume())+'立方厘米')
L_SaveData.append('大礼盒的表面积是:'+str(big_gift_box.area())+'平方厘米')
index=big_gift_box.type.index('大礼盒')
g_box_num=big_gift_box.countBoxnums(200,index)
L_SaveData.append('200条鱼需要'+str(g_box_num)+'只大礼盒')
L_SaveData.append('200条鱼装大礼盒的价值为:'+str(g_box_num*big_gift_box.price)+'元')
print(L_SaveData)
print('--'*15)
small_gift_box=FishBox(50,20,30)  #创建长50cm,宽20cm，高30cm的小礼盒实例
small_gift_box.price=500         #价格500元
small_gift_box.amount=10          #1盒存放10条
small_gift_box.weight=5          #5公斤
L_SaveData.append('小礼盒的体积是:'+str(small_gift_box.volume())+'立方厘米')
L_SaveData.append('小礼盒的表面积是:'+str(small_gift_box.area())+'平安厘米')
index=small_gift_box.type.index('小礼盒')
g_box_num=small_gift_box.countBoxnums(200,index)
L_SaveData.append('200条鱼需要'+str(g_box_num)+'只小礼盒')
L_SaveData.append('200条鱼装小礼盒的价值为:'+str(g_box_num*small_gift_box.price)+'元')
print(L_SaveData)
print('--'*15)
if save_file('fish_records.txt',L_SaveData):
    print('保存成功')
else:
    print('保存失败')