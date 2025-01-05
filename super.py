class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname,self.lname)
class student(person):
    def __init__(self,fname,lname,grade,year):
        self.grade=grade
        self.year=year
        super().__init__(fname,lname)
obj=student("chandu","neeraj",12,2025)
obj.display()
print(obj.year,obj.grade)
