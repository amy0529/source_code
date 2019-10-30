f_n=r'd:\t3.txt'
flag=False
try:
    f=open(f_n,'r')
    print(f.read())
    flag=True
except:
    print('打开%s文件出错,请检查!'%(f_n))
finally:
    if flag:
        f.close()
        print('文件做关闭处理!')
    else:
        print("程序关闭!")
    
