nums=0
amount=0
i=0
fish_records=['1月1日','鲫鱼',18,10.5,'1月1日','鲤鱼',8,6.2,'1月1日','鲢鱼',7,4.7,'1月2日','草鱼',2,7.2,'1月2日','鲫鱼',3,12,'1月2日','黑鱼',6,15,'1月3日','乌龟',1,71,'1月3日','鲫鱼',1,9.8]
print('钓鱼日期 名称  数量 单价(元)')
print('-----------------------------')
while i<len(fish_records):
    nums=nums+fish_records[i+2]
    amount=amount+fish_records[i+2]*fish_records[i+3]
    print('%s , %s ,%.2f , %.2f'%(fish_records[i],fish_records[i+1],fish_records[i+2],fish_records[i+3]))
    i=i+4
print('-----------------------------')
print('        总数:%d,总金额%.2f元'%(nums,amount))


