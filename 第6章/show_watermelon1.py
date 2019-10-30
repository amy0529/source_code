def watermelon(name,**attributes):#带**的为可以传递任意数量"健-值"的参数
    print(name)
    print(type(attributes))       #验证attributes的类型              
    return attributes             #返回字典类型对象
print(watermelon('西瓜',taste='甜',shape='圆形',color='绿色'))
