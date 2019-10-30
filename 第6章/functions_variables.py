j=5                                  #全局变量j

def sum0():
    k=2                              #闭包变量k
    def sum1():
        i=k+j                        #局部变量i
        return i
    return sum1()

print('调用sum0结果%d.'%(sum0()))

