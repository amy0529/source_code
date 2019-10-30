import os
import sys
get_cur_path=os.path.abspath(os.path.curdir)
f_n=get_cur_path+'\\files'
try:
    if not os.path.isdir(f_n):
        os.makedirs(f_n)
except:
    print("子文件夹%s建立出错!")
    sys.exit()
#====================================上面为动态建立文件夹
f_n=f_n+'\\t3.txt'
flag=False
try:
    f=open(f_n,'w')
    print(f.write("OK"))
    flag=True
    print('文件%s写入正常!'%(f_n))
except:
    print('打开%s文件出错,请检查!'%(f_n))
finally:
    if flag:
        f.close()
        print('文件做关闭处理!')
    else:
        print("程序关闭!")
    
