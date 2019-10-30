def find_factor(nums):                 #带参数nums的求因数的自定义函数
    '''
    find_factor是自定义函数
    nums是传递一个正整数的参数
    以字符串形式返回一个正整数的所有因数
    '''
    if type(nums)!=int:
        print('输入值类型出错,必须是整数!')
        return
    if nums<=0:
        print('输入值范围出错,必须正整数!')
        return
    i=1
    str1=''
    while i<=nums:                     #循环求nums的因数
        if nums%i==0:                  #求nums的因数
            str1=str1+' '+str(i)
        i+=1
    return str1             #返回因数
#======================================
find_factor('a')            #传递一个字符a 

#help(find_factor)           #用help函数获取find_factor函数帮助信息
                            #执行结果如下:

#Help on function find_factor in module __main__:

#find_factor(nums)
#    find_factor是自定义函数
#    nums是传递一个正整数的参数
#    以字符串形式返回一个正整数的所有因数
