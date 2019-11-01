nums=[17,8,7,2,3,6,1,1,5]
prices=[10.5,6.2,4.7,7.2,12,15,78.1,10.78,7.92]
amount=sum(nums)
print('鱼总数:%d'%(amount))
total=[x*y for x,y in zip(nums,prices)]
print(sum(total))