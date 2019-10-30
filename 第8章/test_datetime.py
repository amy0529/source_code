from datetime import datetime,date,time

print(datetime.now())         #返回当天的日期和时间
today=datetime.now()
print(datetime.date(today))   #返回当天的日期
print(datetime.time(today))   #返回当天的时间

print(datetime.ctime(today))  #返回"星期,月,日,时,分,秒,年"格式的字符串
print(datetime.utcnow())  #返回当前的UTC日期和时间
print(datetime.timestamp(today)) #返回当天的时间戳
print(datetime.fromtimestamp(datetime.timestamp(today)))#根据时间戳返回 UTC datetime

date1=date(2018,2,12)
time1=time(20,53,48)
print(datetime.combine(date1,time1))#邦定日期,时间,生成新的datetime对象

newDatetime=datetime.strptime("12/2/18 20:59",'%d/%m/%y %H:%M')  #用字符串和指定格式生成新的datetime对象
print(newDatetime)

for tv in datetime.timetuple(today):
    print(tv)
print(today.isocalendar()) #ISO格式的日期
print(today.strftime("%Y年%m月%d日 %H:%M:%S %p"))



