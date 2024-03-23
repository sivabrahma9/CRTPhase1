# class ece:
#     def student1(self,marks):
#         print("student1 good on studies he scored",marks)
#         self.s=marks
#     def student2(self):
#         print('student2 is average in studies')
#         print(self.s)
#     def student3(self):
#         print("very bad student")
# siva=ece()
# siva.student1(90)
# siva.student2()
# siva.student3()


# class shopping:
#     def dresstype1(self,dress):
#         print("which type of dress user wants is",dress)
#         self.d=dress
#     def price1(self,price):
#         print("the price the user wants is",price)
#         self.p=price
#     def size1(self,size):
#         print("the size user wants is",size)
#         self.s=size
#     def display(self):
#         print(self.d)
#         print(self.p)
#         print(self.s)
# l=shopping()
# l.dresstype1("shirt")
# l.price1(3000)
# l.size1("m")
# l.display()






# class shopping(ece):
#     def __init__(self,location):
#         self.l=location
#         print("welcome to ",location)
#     def dresstype1(self,dress):
#         print("which type of dress user wants is",dress)
#         self.d=dress
#     def price1(self,price):
#         print("the price the user wants is",price)
#         self.p=price
#     def size1(self,size):
#         print("the size user wants is",size)
#         self.s=size
#     def display(self):
#         print(self.d)
#         print(self.p)
#         print(self.s)
#         print(self.l)
# l=shopping("RARERABBIT")
# l.dresstype1("shirt")
# l.price1(3000)
# l.size1("m")
# l.display()
# l.student1(20)
# l.student2()
# l.student3()




# class shopping(ece):
#     def __init__(self,location):
#         self.l=location
#         print("welcome to ",location)
#     def dresstype1(self,dress):
#         print("which type of dress user wants is",dress)
#         self.d=dress
#     def price1(self,price):
#         print("the price the user wants is",price)
#         self.p=price
#     def size1(self,size):
#         print("the size user wants is",size)
#         self.s=size
#     def display(self):
#         print(self.d)
#         print(self.p)
#         print(self.s)
#         print(self.l)
# l=shopping("RARERABBIT")
# l.student1(20)
# l.student2()
# l.student3()


####   MULTILEVEL INHERITANCE
# class placements:
#     def info(self):
#         print("1062")
# class dept(placements):
#     def display(self):
#         print("all depts")
# class pragati(dept):
#     def welcome(self):
#         print("welcome")
# ob=pragati()
# ob.info()
# ob.display()
# ob.welcome()


### HIEARACHAL INHERITANCE
# class placements:
#     def info(self):
#         print("1062")
# class dept(placements):
#     def display(self):
#         print("all depts")
# class pragati(placements):
#     def welcome(self):
#         print("welcome")
# ob=pragati()
# ob.info()
# ob.welcome()


### MULTIPLE INHERITANCE

# class placements:
#     def info(self):
#         print("1062")
# class dept:
#     def display(self):
#         print("all depts")
# class pragati(dept,placements):
#     def welcome(self):
#         print("welcome")
# ob=pragati()
# ob.info()
# ob.welcome()
# ob.display()

### HYBRID INHERITANCE

# class placements:
#     def info(self):
#         print("1062")
# class dept(placements):
#     def display(self):
#         print("all depts")
# class pragati(dept,placements):
#     def welcome(self):
#         print("welcome")
# ob=pragati()
# ob.info()
# ob.welcome()
# ob.display()

#### function overriding
# class father:
#     def bike(self):
#         print("bullet")
#     def laptop(self):
#         print("laptop")
# class son(father):
#     def laptop(self):
#         print("macbook")
# obj=son()
# obj.bike()
# obj.laptop()


#### constructor overriding
# class father:
#     def __init__(self):
#         print("father i am done")
# class child(father):
#     def __init__(self):
#         print("child:you are not done dad")
# obj=child()


###ABSTRACTION

# class polygon(ABC):
#     @abstractmethod
#     def noofsides(self):
#         pass
# class 
    


# class carshowroom:
#     def __init__(self):
#         default()
#     def company(self,car):
#         print("wlcome to ",car)
#     def model(self)
#         list["benz","audi","volkswagon"]
#         print()


