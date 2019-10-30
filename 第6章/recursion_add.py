def recursion_sum(num):                #定义自定义递归函数
    if num==1:                         #分解到最小数1,
        return num                     #返回最小分解数1给上一层
    return recursion_sum(num-1)+num    #自己调用自己,重复动作,两个相邻数相加

print(recursion_sum(4))                #调用递归函数,并打印结果

