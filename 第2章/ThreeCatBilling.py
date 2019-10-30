num1,num2,num3=5,6,9
price1,price2,price3=8.1,8.2,8
fish1,fish2,fish3='鲫鱼','鲤鱼','草鱼'
date='2017年12月'
Total_Num=num1+num2+num3      #总的鱼数
Total_Amount=num1*price1+num2*price2+num3*price3 #总金额
print("-----"*4+"三酷猫记账单"+"-----"*4)
print('钓鱼地点   '+'钓鱼日期   '+'   鱼名  '+'数量（条）'+' 单价（元）')
print('左小河    '+date+'1日 '+fish1+'  '+str(num1)+'         '+str(price1))
print('右小河    '+date+'2日 '+fish2+'  '+str(num2)+'         '+str(price2))
print('长  江    '+date+'3日 '+fish3+'  '+str(num3)+'         '+str(price3))
print("----"*12+'--')
print('鱼数总计%d条，市场价格总计%.2f元，每天平均钓鱼数量约%d条(%f条)'
      %(Total_Num,Total_Amount,int(Total_Num/3),Total_Num/3))



      

