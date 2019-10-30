nums=['one','two','three','four','five','six','seven']
t=open(r'd:\t2.txt','a')
for get_one in nums:
    t.write(get_one+'\n')
t.close()
print('连续写入完成!')
#=========================一次读一行
t1=open(r'd:\t2.txt','r')
dd=1
while dd :
    dd=t1.readline()
    print(dd)
#=========================以列表格式读取多行
t1=open(r'd:\t2.txt','r')
L_s=t1.readlines()
print(L_s)

