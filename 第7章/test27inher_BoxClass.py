class Box1(object):           #2.7版本必须加Object参数                        
    '''box1'''
    def  __init__(self,length1,width1,height1): 
        self.length=length1                   
        self.width=width1                     
        self.height=height1
    def volume(self):                        
        return self.length*self.width*self.height


class Box2(Box1):                             
    def __init__(self,length1,width1,height1): 
        #super().__init__(length1,width1,height1) 
        super(Box2,self).__init__(length1,width1,height1) #(length1,width1,height1) #必须加2个参数
        self.color='white'                      
        self.material='paper'                   
        self.type='fish'                         
    def area(self):
        result=self.length*self.width*2+self.length*self.height*2+self.width*self.height*2
        return result
    def volume(self,num=1):
         return self.length*self.width*self.height*num
my_box1=Box2(2,2,2)
print(my_box1.area()) 
#my_box1=Box2(1,2,1)        
#my_box2=Box2(10,10,10)                       
#print('cube%d'%(my_box2.volume()))  
#print('cube%d'%(my_box2.area()))
#print('cube%s,%s,%s'%(my_box2.color,my_box2.material,my_box2.type))
#print('cube%d'%(my_box2.volume(5)))
