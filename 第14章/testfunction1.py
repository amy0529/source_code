import math
def sums(*num):
    total=sum(num)
    print("累加为：%f"%total)
if __name__ == "__main__":
    import doctest
    doctest.testfile('test_content.txt',verbose=False)
