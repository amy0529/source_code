class StaticC():
    name='Tom'                             #类局部变量name,没有定义属性的说法
    age=20                                 #类局部变量age
    address='China'                        #类局部变量address
    call=28380000#类局部变量call
    def a():                               #函数a，没有使用self参数，不能叫方法
        i=0
        i+=1
        print('第一个函数%d'%(i))

    def b(add=1):                          #函数b
        print('第二个函数%d'%(add))
    def c(add=1):#函数c
        print('第三个函数%d'%(add))
        return add
    
StaticC.c()
