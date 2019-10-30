def watermelon(name,attributes):   #传递元组,列表,字典
    print(name)
    print(type(attributes))       #验证attributes的类型              
    return attributes             #返回对应类型对象
get_t=watermelon('西瓜',('甜','圆形','绿色'))
print(get_t)                      #打印返回的对象
get_L=watermelon('西瓜',['甜','圆形','绿色'])
print(get_L)                      #打印返回的对象
attri={'taste':'甜','shape':'圆形','color':'绿色'}
get_D=watermelon('西瓜',attri)
print(get_D)
