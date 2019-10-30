d_date1={'鲫鱼':[18,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]}     #1月1日钓鱼记录
d_date2={'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]}         #1月2日钓鱼记录
d_date3={'乌龟':[1,71],'鲫鱼':[1,9.8],'草鱼':[5,7.2],'黄鱼':[2,40]}#1月3日钓鱼记录
fish_records={'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}  #所有钓鱼记录 
nums=0          #钓鱼总数量初始化定义
amount=0        #钓鱼总金额初始化定义
day=''          #日期记录变量初始化定义
day_record={}   #钓鱼每天记录字典变量初始化定义
for day,day_record in fish_records.items():    #循环获取每天记录(元组形式)
    print('%s钓鱼记录为:'%(day))              #打印当天的日期
    for name,sub_recods in day_record.items(): #循环获取当天鱼与数量,单价关系的记录
        nums+=sub_recods[0]                    #数量累加
        amount+=sub_recods[0]*sub_recods[1]    #金额累加
        print('    %s数量%d,单价%.2f元'%(name,sub_recods[0],sub_recods[1]))#打印名称,数量,单价
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amount)) #打印总数量,总金额

