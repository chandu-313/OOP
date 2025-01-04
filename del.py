class student:
    def __init__(self):
     print("The Student has created")
    def __del__(self):
     print("the object has been deleted")
obj=student()
del obj
print(obj)