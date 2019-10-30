import math
def sums(*num):
    '''
    >>> sums(1,2,3,4,5)
    15
    >>> sums('s',2,3,4,5)
    '''
    total=sum(num)
    print("累加为：%f"%total)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
