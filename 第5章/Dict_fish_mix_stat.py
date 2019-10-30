d_date1={'三酷猫':{'鲫鱼':[17,10.5],'鲤鱼':[8,6.2],'鲢鱼':[7,4.7]},'加菲猫':{'黑鱼':[8,16]},'大脸猫':{'草鱼':[12,8]}}     #1月1日钓鱼记录
d_date2={'三酷猫':{'草鱼':[2,7.2],'鲫鱼':[3,12],'黑鱼':[6,15]},'加菲猫':{'鲤鱼':[9,7.1]}}         #1月2日钓鱼记录
d_date3={'三酷猫':{'乌龟':[1,78.10],'鲫鱼':[1,10.78],'草鱼':[5,7.92]},'大脸猫':{'鲫鱼':[8,9.8],'螃蟹':[5,15]}}        #1月3日钓鱼记录
fish_records={'1月1日':d_date1,'1月2日':d_date2,'1月3日':d_date3}  #所有钓鱼记录 
nums=0          #钓鱼总数量初始化定义
amount=0        #钓鱼总金额初始化定义
day=''          #日期记录变量初始化定义

#==============================================按鱼名进行数量,金额累计
print('=========每日钓鱼记录==========')
for day,day_record in fish_records.items():    #循环获取每天记录(元组形式)
    if nums>0:
        print('-----------------')
    day_nums=0      #每天钓鱼数量
    day_amount=0    #每天钓鱼金额
    print('%s钓鱼记录为:'%(day))               #打印当天的日期
    for name1,get_fish_record1_d in day_record.items(): #循环获取当天钓鱼记录
        print('   %s:'%(name1))                     #打印钓鱼者
        for name2,get_fish_record2_d in get_fish_record1_d.items():    #获取鱼名和对应值（列表）
            day_nums+=get_fish_record2_d[0]                            #当天数量累加
            day_amount+=get_fish_record2_d[0]*get_fish_record2_d[1]    #当天金额累加
            print('      %s数量%d,单价%.2f元'%(name2,get_fish_record2_d[0],get_fish_record2_d[1]))#打印名称,数量,单价
    print('%s,钓鱼数量为%d,金额为%.2f元'%(day,day_nums,day_amount))    #打印当天钓鱼数量、金额
    nums+=day_nums                                                     #所有数量累加
    amount+=day_amount                                                 #所有金额累加
print('========统计结果打印=========')

print('钓鱼总数量为%d,总金额为%.2f元'%(nums,amount)) #打印总数量,总金额

=========每日钓鱼记录==========
1月1日钓鱼记录为:
   三酷猫:
      鲫鱼数量17,单价10.50元
      鲤鱼数量8,单价6.20元
      鲢鱼数量7,单价4.70元
   加菲猫:
      黑鱼数量8,单价16.00元
   大脸猫:
      草鱼数量12,单价8.00元
1月1日,钓鱼数量为52,金额为485.00元
-----------------
1月2日钓鱼记录为:
   三酷猫:
      草鱼数量2,单价7.20元
      鲫鱼数量3,单价12.00元
      黑鱼数量6,单价15.00元
   加菲猫:
      鲤鱼数量9,单价7.10元
1月2日,钓鱼数量为20,金额为204.30元
-----------------
1月3日钓鱼记录为:
   三酷猫:
      乌龟数量1,单价78.10元
      鲫鱼数量1,单价10.78元
      草鱼数量5,单价7.92元
   大脸猫:
      鲫鱼数量8,单价9.80元
      螃蟹数量5,单价15.00元
1月3日,钓鱼数量为20,金额为281.88元
========统计结果打印=========
钓鱼总数量为92,总金额为971.18元
