Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
#复制列表
>>> vegetables=['白菜','萝卜','青菜','芹菜','花菜','白菜']
>>> id(vegetables)

42718272
>>> new_vege=vegetables.copy()
>>> id(new_vege)
42718112
>>> same_list=vegetables
>>> id(same_list)
42718272
>>> 
#排序
>>> fruit=['banana','pear','apple','peach']
>>> fruit_l=fruit.copy()
>>> fruit_l.sort()
>>> print(fruit_l)
['apple', 'banana', 'peach', 'pear']
>>> fruit_h=fruit.copy()
>>> fruit_h.sort(reverse=True)
>>> print(fruit_h)
['pear', 'peach', 'banana', 'apple']
#小写排序
>>> listA=['Tom','tim','john','Jack']
>>> listA1=listA.copy()
>>> listA1.sort()
>>> print(listA1)
['Jack', 'Tom', 'john', 'tim']
>>> listB=listA.copy()
>>> listB.sort(key=str.lower)
>>> print(listB)
['Jack', 'john', 'tim', 'Tom']
