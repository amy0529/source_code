def watermelon(name,*attributes):#带*的为可以传递任意数量值的参数
    print(name)
    print(type(attributes))      #验证attributes的类型
    description=''              
    for get_t in attributes:     #暗示是以集合数据类型进行操作  
        description+=' '+get_t       #形成字符串属性说明内容
    print(description)           #打印属性说明
watermelon('西瓜','甜','圆形','绿色')
print('---------------------')
watermelon('西瓜','甜','圆形','绿皮','红瓤','无籽')
