'''
    >>> sums(1,2,3,4,5)
    15
    >>> sums('a'2,3,4,5)
    14
    '''
import math                             #导入math模块
def sums(*num):                         #自定义函数，传递元组数字
    
    total=math.trunc(sum(num))          #对元组元素求和
    return total
    print(total)         #打印累计结果
if __name__ == "__main__":
    import doctest                 #导入doctest模块
    doctest.testmod(verbose=True) #调用testmod()，读取2用例，测试上述函数
