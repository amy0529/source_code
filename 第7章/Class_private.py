class TeatPrivate():
    
    def __init__(self):
        self.__say='ok'  #__say属性实例无法看到
    def p(self):
       print(self.__say)
    def __p1(self):      #__p1()方法实例无法看到
       print(self.__say)
       
show=TeatPrivate()
show.p()


