from Class_module import FishBox
#===============================创建大礼盒实例，并求相关值
big_gift_box=FishBox(60,30,40)  #创建长60cm,宽30cm，高40cm的大礼盒实例
big_gift_box.price=1000         #价格1000元
big_gift_box.amount=20          #1盒存放20条
big_gift_box.weight=10          #10公斤
print("大礼盒的体面积是%d立方厘米"%(big_gift_box.volume()))
print("大礼盒的表面积是%d平方厘米"%(big_gift_box.area()))
index=big_gift_box.type.index('大礼盒')
print(index)
g_box_num=big_gift_box.countBoxNums(200,index)
print("200条鱼需要%d只大礼盒"%(g_box_num))
print("200条鱼装大礼盒的价值为%d元"%(g_box_num*big_gift_box.price))
#===============================创建小礼盒实例，并求相关值
small_gift_box=FishBox(50,20,30)  #创建长50cm,宽20cm，高30cm的小礼盒实例
small_gift_box.price=500         #价格500元
small_gift_box.amount=10          #1盒存放10条
small_gift_box.weight=5          #5公斤
print("小礼盒的体面积是%d立方厘米"%(small_gift_box.volume()))
print("小礼盒的表面积是%d平方厘米"%(small_gift_box.area()))
index=small_gift_box.type.index('小礼盒')
g_box_num=small_gift_box.countBoxNums(200,index)
print("200条鱼需要%d只小礼盒"%(g_box_num))
print("200条鱼装小礼盒的价值为%d元"%(g_box_num*small_gift_box.price))
