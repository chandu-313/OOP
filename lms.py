class library:
    def __init__(self,name,list):
        self.name=name
        self.list=list
        self.dict={}
    def display(self):
        print("welcome to the library",self.name)
        print("we have following books in our library")
        for i in self.list:
            print(i)
    def lendbook(self,name,book):
        if book not in self.dict:
            self.dict.update({book:name})
            print("your name is registered")
            self.list.remove(book)
        else:
            print("book is already in use")
    def addbook(self,book):
        self.list.append(book)
        print("your book is successfully added")
obj=library("BookHub",["R.S Agarwal","R.D Sharma","Physics Wallah","Bhagavath Gita"])
while True:
    print("welcome to",obj.name)
    print("press 1 for display")
    print("press 2 for add book")
    print("press 3 for remove book")
    choice=int(input("enter your choice"))
    if choice==1:
        obj.display()
    elif choice==2:
        name=input("enter the username")
        book=input("enter the name of the book")
        obj.lendbook(name,book)
    elif choice==3:
        book=input("enter book name")
        obj.addbook(book)
    print("Press q to quit and c to continue")

    user_choice2 = ""

    while (user_choice2 != "c" and user_choice2 != "q"):

        user_choice2 = input()

        if user_choice2 == "q":

              exit()

        elif user_choice2 == "c":

         continue