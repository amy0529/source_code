def print_D(dic):
    i=0
    len1=len(dic)
    while i<len1:
        print(dic.popitem())
        i+=1
        
print_D({1:'a',2:'b'})  #正常字典对象

print_D([1,2,3])        #错误传输对象
