import sys
# sys.path[0]='X:\github\source_code\\amy_test\module'
# print(sys.path)
from Class_module import FishBox

big_gif_box=FishBox(60,30,40)
big_gif_box.price=1000
big_gif_box.amount=20
big_gif_box.weight=10
print('大礼盒的体面积是%d立方厘米'%(big_gif_box.volume()))
print('大礼盒的表面积是%d平方厘米'%big_gif_box.area())
index=big_gif_box.type.index('大礼盒')
g_box_num=big_gif_box.countBoxnums(200,index)
print('200条鱼需要%d只大礼盒'%(g_box_num))
print(g_box_num)
print('200条鱼装大礼盒的价值为%d元'%(g_box_num*big_gif_box.price))
small_gif_box=FishBox(50,20,30)
small_gif_box.price=500
small_gif_box.amount=10
small_gif_box.weight=5
print('小礼盒的体面积是%d立方厘米'%(small_gif_box.volume()))
print('小礼盒的表面积是%d平方厘米'%small_gif_box.area())
index=small_gif_box.type.index('小礼盒')
print(index)
small_box_num=big_gif_box.countBoxnums(200,index)
print(small_box_num)
print('200条鱼需要%d只大礼盒'%(small_box_num))
print('200条鱼装小礼盒的价值为%d元'%(small_gif_box.price*small_box_num))
