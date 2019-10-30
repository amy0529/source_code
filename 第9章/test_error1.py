import sys
try:
	1/0    #除数为0错误
except:
    print("除数不能为0")
    sys.exit()
finally:
    print("程序执行结束!")
print("我能执行么?")
