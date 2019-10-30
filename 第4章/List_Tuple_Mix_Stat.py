fish_tuple=('鲫鱼','鲤鱼','鲢鱼','草鱼','黑鱼','乌龟')
fish_sum=[0,0,0,0,0,0,0,0,0,0,0,0]  #记录每种水产品的数量和金额
fish_records=['1月1日','鲫鱼',18,10.5,'1月1日','鲤鱼',8,6.2,'1月1日','鲢鱼',7,4.7,'1月2日','草鱼',2,7.2,'1月2日','鲫鱼',3,12,'1月2日','黑鱼',6,15,'1月3日','乌龟',1,71,'1月3日','鲫鱼',1,9.8]
fish_records[2]-=1  #减去野猫叼走的那一条
#-------------------修改黑鱼升值价格
i=1
fishs_len=len(fish_records)
while i<fishs_len:
    if fish_records[i]=='黑鱼':
        fish_records[i+1]=fish_records[i+1]*1.1  #黑鱼都升值10%
    i+=4                                         #循环变量控制
#-------------------统计每种水产品的数量和金额
i=0
while i<fishs_len:
    if fish_tuple[0]==fish_records[i+1]:         #统计鲫鱼
        fish_sum[0]+=fish_records[i+2]           #记录数量
        fish_sum[1]+=fish_records[i+2]*fish_records[i+3]#记录金额
    elif fish_tuple[1]==fish_records[i+1]:       #统计鲤鱼
        fish_sum[2]+=fish_records[i+2]           #记录数量
        fish_sum[3]+=fish_records[i+2]*fish_records[i+3]#记录金额
    elif fish_tuple[2]==fish_records[i+1]:       #统计鲢鱼
        fish_sum[4]+=fish_records[i+2]           #记录数量
        fish_sum[5]+=fish_records[i+2]*fish_records[i+3]#记录金额
    elif fish_tuple[3]==fish_records[i+1]:       #统计草鱼
        fish_sum[6]+=fish_records[i+2]           #记录数量
        fish_sum[7]+=fish_records[i+2]*fish_records[i+3]#记录金额
    elif fish_tuple[4]==fish_records[i+1]:       #统计黑鱼
        fish_sum[8]+=fish_records[i+2]           #记录数量
        fish_sum[9]+=fish_records[i+2]*fish_records[i+3]#记录金额
    elif fish_tuple[5]==fish_records[i+1]:       #统计乌鱼
        fish_sum[10]+=fish_records[i+2]           #记录数量
        fish_sum[11]+=fish_records[i+2]*fish_records[i+3]#记录金额
    i+=4                                         #循环变量控制
j=0
amount=0            #销售额初始化赋值
total_nums=0        #总数量初始化赋值
while j<len(fish_sum):
    if j%2==0:
       total_nums+=fish_sum[j]
    else:
       amount+=fish_sum[j]
    j+=1

#-------------------核算成本,求纯利润
cost=180+20+1+amount*0.05     #求成本
profit=amount-cost            #求纯利润
#-------------------打印三酷猫花样统计结果
i=0

while i<len(fish_tuple):
    print('%s总数是%d ,金额是%f'%(fish_tuple[i],fish_sum[i*2],fish_sum[i*2+1]))
    i+=1
print('-'*30)
print('三酷猫总共钓上%d条水产品,预计销售额为%.2f元,成本为%.2f元,利润为%.2f元'%(total_nums,amount,cost,profit))
#==============================执行结果如下
鲫鱼总数是21 ,金额是224.300000
鲤鱼总数是8 ,金额是49.600000
鲢鱼总数是7 ,金额是32.900000
草鱼总数是2 ,金额是14.400000
黑鱼总数是6 ,金额是99.000000
乌龟总数是1 ,金额是71.000000
------------------------------
三酷猫总共钓上45条水产品,预计销售额为491.20元,成本为225.56元,利润为265.64元

