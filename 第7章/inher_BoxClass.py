class Box1():                                   #定义父类Box1
    '''求立方体的类'''
    def  __init__(self,length1,width1,height1): 
        self.length=length1                   
        self.width=width1                     
        self.height=height1
    def volume(self):                        
        return self.length*self.width*self.height


class Box2(Box1):                             #继承Box1定义子类Box2
    def __init__(self,length1,width1,height1): #子类也是__init__开始,可以从父类原样拷贝代码
        super().__init__(length1,width1,height1) #super实现父类与子类的关联,继承父类的属性
        self.color='white'                       #增加颜色属性
        self.material='paper'                    #增加材质属性
        self.type='fish'                         #增加类型属性
    def area(self):
        result=self.length*self.width*2+self.length*self.height*2+self.width*self.height*2
        return result
    def volume(self,num=1):
         return self.length*self.width*self.height*num
     
my_box2=Box2(10,10,10)                       #通过子类Box2创建my_box2实例
print('立方体体积是%d'%(my_box2.volume()))   #通过实例调用volume()求体积，并打印
print('立方体表面积是%d'%(my_box2.area()))
print('立方体的颜色是%s,材质是%s,类型是%s'%(my_box2.color,my_box2.material,my_box2.type))
print('5个立方体体积是%d'%(my_box2.volume(5)))
