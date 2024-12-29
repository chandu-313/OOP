class eagle:
  species="bird"
  def __init__(self,name,age):
    self.name=name
    self.age=age
ob=eagle("max",7)
ob2=eagle("mario",11)
print("we are having two birds",ob.name,ob2.name)
print("the ages of the birds are",ob.age,ob2.age)
print("both are associated with with the species",ob.species,ob2.species)
