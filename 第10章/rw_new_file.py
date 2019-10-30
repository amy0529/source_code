#==========================================往文件里写内容
newfile=r'd:\t1.txt'                       #定义需要建立的文本名称和路径
b_new_file=open(newfile,'w')               #用open函数建立一个新的文本文件
t_n=b_new_file.write('I like python!')     #用文件对象write()方法写字符串
b_new_file.close()                         #用close()方法关闭新建的文件
print("往文件里写入%d字节内容"%(t_n))      #提示写文本文件内容成功
#==========================================往文件里读内容
b_new_file=open(newfile,'r')             #以只读方式打开t1.txt文件
tt=b_new_file.read()                     #用文件对象read()方法读取内容
print(tt)                                #打印读取内容
b_new_file.close()                       #关闭打开的文件

#==========================================可读写方式打开文件,并读写内容
b_new_file=open(newfile,'r+')             #以只读方式打开t1.txt文件
tt=b_new_file.read()                     #用文件对象read()方法读取内容
print(tt)                                #打印读取内容
t_n=b_new_file.write('\n三酷猫!^_^')
b_new_file.close()                       #关闭打开的文件
print("往文件里写入%d字节内容"%(t_n))      #提示写文本文件内容成功


