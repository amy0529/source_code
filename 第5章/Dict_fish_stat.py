d_date1={'鲫鱼':[17,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]}     #1月1日钓鱼记录
d_date2={'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]}         #1月2日钓鱼记录
d_date3={'乌龟':[1,78.10],'鲫鱼':[1,10.78],'草鱼':[5,7.92]}        #1月3日钓鱼记录
fish_records={'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}  #所有钓鱼记录 
nums=0          #钓鱼总数量初始化定义
amount=0        #钓鱼总金额初始化定义
day=''          #日期记录变量初始化定义
day_record={}   #钓鱼每天记录字典变量初始化定义
stat_record={}  #统计记录变量初始化定义
name_n=''       #最大数量的鱼
max_nums=0      #最大数量
name_a=''       #最大金额的鱼
max_amount=0    #最大金额
#==============================================按鱼名进行数量,金额累计
print('=========每日钓鱼记录==========')
for day,day_record in fish_records.items():    #循环获取每天记录(元组形式)
    print('%s钓鱼记录为:'%(day))              #打印当天的日期
    for name,sub_recods in day_record.items(): #循环获取当天鱼与数量,单价关系的记录
        nums+=sub_recods[0]                    #数量累加
        amount+=sub_recods[0]*sub_recods[1]    #金额累加
        print('    %s数量%d,单价%.2f元'%(name,sub_recods[0],sub_recods[1]))#打印名称,数量,单价
        if name in stat_record:                #判断鱼是否在统计字典里,在,则做累计处理
            stat_record[name][0]+=sub_recods[0]#每种鱼数量累计
            stat_record[name][1]+=sub_recods[0]*sub_recods[1]#每种鱼金额累计
        else:
            stat_record[name]=[sub_recods[0],sub_recods[0]*sub_recods[1]]#第一次累计,直接在字典里赋值
#==============================================在统计记录字典变量里找最大值
print('=====按鱼进行数量,金额统计=====')
for name1,get_L in stat_record.items():
    print('%s的总数量%d,金额为%.2f元'%(name1,get_L[0],get_L[1]))
    get_nums_d={name1:get_L[0]}
    if get_L[0]>max_nums:                      #寻找最大数量的鱼
        name_n=name1
        max_nums=get_L[0]
    get_amount_d={name1:get_L[1]}        
    if get_L[1]>max_amount:                    #寻找最大金额的鱼
        name_a=name1
        max_amount=get_L[1]
#==============================================统计结果打印
print('====最大值,总数量,总金额统计====')
print('最大数量的鱼是%s,%d条'%(name_n,max_nums))
print('最大金额的鱼是%s,%.2f元'%(name_a,max_amount))
print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amount)) #打印总数量,总金额

=========每日钓鱼记录==========
1月1日钓鱼记录为:
    鲫鱼数量17,单价10.50元
    鲤鱼数量8,单价6.20元
    鲢鱼数量7,单价4.70元
1月2日钓鱼记录为:
    草鱼数量2,单价7.20元
    鲫鱼数量3,单价12.00元
    黑鱼数量6,单价15.00元
1月3日钓鱼记录为:
    乌龟数量1,单价78.10元
    鲫鱼数量1,单价10.78元
    草鱼数量5,单价7.92元
=====按鱼进行数量,金额统计=====
鲫鱼的总数量21,金额为225.28元
鲤鱼的总数量8,金额为49.60元
鲢鱼的总数量7,金额为32.90元
草鱼的总数量7,金额为54.00元
黑鱼的总数量6,金额为90.00元
乌龟的总数量1,金额为78.10元
====最大值,总数量,总金额统计====
最大数量的鱼是鲫鱼,21条
最大金额的鱼是鲫鱼,225.28元
钓鱼总数量为50,总金额为529.88元
