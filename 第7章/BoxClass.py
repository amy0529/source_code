class Box1():         #只有函数的类，类名为Box1
    '''求立方体的类'''
    def  __init__(self,length1,width1,height1): #默认传递类参数的保留函数__init__
        self.length=length1                   #self代表实例对象，在实例调用时传递实例对象
        self.width=width1                     #若要在实例里使用类定义的函数或变量，必须通过self才能使用
        self.height=height1
    def volume(self):                        #求立方体体积的函数volume
        return self.length*self.width*self.height
my_box1=Box1(10,10,10)                       #my_box1通过Box1类赋值建立对应的一个实例
print('立方体体积是%d'%(my_box1.volume()))   #通过实例调用volume()求体积，并打印
tt=my_box1.length
print(tt)
