def print_D(dic):
    i=0
    try:
        len1=len(dic)
        while i<len1:
            print(dic.popitem())
            i+=1
    except:
        print("传递值类型出错,必须为字典型!")
        
print_D({1:'a',2:'b'})  #正常字典对象

print_D([1,2,3])        #错误传输对象
