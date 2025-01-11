class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am {self.name}")
        print(f"i am {self.age} year old")
    def make_sound(self):
        print("bark")
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"i am a cat, my name is {self.name}")  
        print(f"i am {self.age} years old") 
    def make_sound(self):
        print("meow")
obj=dog("max",3) 
obj1=cat("stuart",4) 
for i in (obj,obj1):
    i.info()
    i.make_sound()
