class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name,self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary):
        self.salary=salary
        person.__init__(self,name,idnumber)
obj=employee(31436,"akash",1000000)
obj.display()
print(obj.salary)