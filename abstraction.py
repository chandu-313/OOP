from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("human can walk and run")
class lion(animal):
    def move(self):
        print("lion can run")
class fish(animal):
    def move(self):
        print("fish can swim")
obj=human()
obj.move()
obj1=lion()
obj1.move()
obj2=fish()
obj2.move()
