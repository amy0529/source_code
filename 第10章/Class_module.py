#===========================7.3节,继承\重写方法
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
    def volume(self,num=1):                      #重写volume()方法   
         return self.length*self.width*self.height*num
#==========================7.6.1节,增加一个静态类
#class SHost():
#    name='Tom'                            #类局部变量name, 
#    age=20                              #类局部变量age
#    address='china'                       #类局部变量address
#    call='28320000'                             #类局部变量call
#==========================7.7节,继承实现鱼盒类
class FishBox(Box2):
    def __init__(self,length1,width1,height1):
        super().__init__(length1,width1,height1)
        self.price=0                      #价格
        self.amount=0                     #数量
        self.type=('大礼盒','小礼盒')     #重写盒子类型
        self.weight=0                     #重量
    def countBoxNums(self,fish_nums,f_type_index):#根据鱼数量和盒子类型统计盒子数
        if f_type_index==0:               #盒子类型下标值
            self.amount=20                #20条1盒
        else:
            self.amount=10                #10条1盒
        if fish_nums%self.amount==0:  #整除
            return  fish_nums/self.amount
        else:                         #不整除，加1盒
            return  fish_nums/self.amount+1
    def total(self,box_nums,price):
        return box_nums*prcie
        
        
