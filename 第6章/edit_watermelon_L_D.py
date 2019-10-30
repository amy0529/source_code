def EditFrult(name,attributes):   #传递列表,字典
    attributes[0]=attributes[0]*0.9  #打九折
    print(id(attributes)) 
    return attributes             #返回对应类型对象

attri_L=[21,'甜','圆形','绿色']  # 21为价格

get_L=EditFrult('西瓜',attri_L.copy()) #也可以采用attri_L[:]方式获取列表对象副本

#get_L=EditFrult('西瓜',attri_L)
print(get_L)                      #打印返回的对象
print(attri_L)                   #打印原始列表对象
print(id(attri_L))          
