class computer:
    def __init__(self):
        self.__maxprice=1000
    def info(self):
        print(self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
obj=computer()
obj.info()
obj.__maxprice=9999
obj.info()
obj.setmaxprice(990)
obj.info()
