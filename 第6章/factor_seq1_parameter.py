def find_factor(nums):                    #带参数nums的求因数的自定义函数
    i=1
    str1=''
    print('%d的因数是:'%(nums))
    while i<=nums:                     #循环求10的因数
        if nums%i==0:                  #能整除10的整数是10的因数
            str1=str1+' '+str(i)
        i+=1
    print(str1)             #打印因数
#======================================
num2_L=[10,15,18,25]                   #定义四个整数的列表
i=0
num_len=len(num2_L)
while i<num_len:
    find_factor(num2_L[i])             #循环调用find_factor(nums)
    i+=1


