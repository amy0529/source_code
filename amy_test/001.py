import os
import sys
get_cur_path=os.path.abspath(os.path.curdir)
f_n=get_cur_path+'\\files'
print(f_n)
try:
    if not os.path.isdir(f_n):
        print(os.path.isdir(f_n))
except:
    print('子文件夹%s建立出错'%(f_n))
    sys.exit()
print('--'*15)
f_n=f_n+'\\t3.txt'
flag=False
try:
    f=open(f_n,'w')
    print(f.write('OK'))
    flag=True
    print('文件%s写入正常'%(f_n))
except:
    print('打开文件%s出错'%(f_n))
finally:
    if flag:
        f.close()
        print('关闭文件')
    else:
        print('关闭程序')
