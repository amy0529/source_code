def factor_no_para(): #不带参数的求因数的自定义函数
    i=1
    nums=10
    print('%d的因数是:'%(nums))
    while i<=nums:
        if nums%i==0:
            print('%d'%(i))
        i+=1
factor_no_para()     #调用自定义函数
tt=type(factor_no_para) #检查是否是函数类型
print(tt)               #打印tt类型

