from Class_module import *                   #*代表导入所有类
       
my_box2=Box2(10,10,10)                       #通过子类Box2创建my_box2实例
print('立方体体积是%d'%(my_box2.volume()))   #通过实例调用volume()求体积，并打印
print('立方体表面积是%d'%(my_box2.area()))
print('立方体的颜色是%s,材质是%s,类型是%s'%(my_box2.color,my_box2.material,my_box2.type))
print('5个立方体体积是%d'%(my_box2.volume(5)))
