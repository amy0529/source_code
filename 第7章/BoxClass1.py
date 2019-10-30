class Box1():         #类名为Box1
    '''求立方体的类'''
    def __init__(self):
        self.length=0
        self.width=0
        self.height=0
        

        
    def volume(self):                        #求立方体体积的函数volume
        return self.length*self.width*self.height
my_box1=Box1()                                #my_box1通过Box1类赋值建立对应的一个实例
my_box1.length=10
my_box1.width=10
my_box1.height=10
print('立方体体积是%d'%(my_box1.volume()))   #通过实例调用volume()求体积，并打印
