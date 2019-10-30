def r_dichotomy(nums,find,left,right):
    middle=(right+left)//2   #求商的整数,取中间值的下标
    if nums[middle]==find: #找到列表中的值    
        return middle     #返回找到值对应的下标
    if right==left+1 :    #若指定范围只有一个未找元素
        if nums[middle]!=find: #而且没有找到
            return -1     #返回-1,-1代表没有找到
    if nums[middle]>find: #值的查找范围在[0,middle)之间
        return r_dichotomy(nums,find,left,middle) #在下标范围在[0,middle)之间的子列表里查找
    elif nums[middle]<find: #值的查找范围在(middle,最大值下标]之间
        return r_dichotomy(nums,find,middle+1,right) #在下标范围在(middle,最大值下标]之间的子列表里查找
nums_L=[1,2,3,4,8,16,20,30]  #元素排序的列表

print(r_dichotomy(nums_L,20,0,len(nums_L))) #在列表里查找值为20的元素的下标
