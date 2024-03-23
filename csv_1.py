# import csv 
# f=open("student.csv","a",newline="")
# a=csv.writer(f)
# a.writerow(["studentid","rollno","name"])
# studentid=int(input("enter student id:"))
# roolno=int(input("enetr your roll no:"))
# name=input("enter your name:")
# a.writerow(["studentid","rollno","name"])
# print("student record has save")


# with open()
# class carshowroom:
#     def __init__(self):
#         default()
#     def company(self,car):
#         print("welcome to ",car)
#     def model(self)
#         list["benz","audi","volkswagon"]
#         print()
    

class carshowroom:
    def _init_(self):
        self.sgst=5055
        self.cgst=600
        self.insurance=6000
    def company(self):
        print("tata,tayota,mercedes")
        self.n=input("enter a company:")
        while True:
            if self.n=="tayota":
                print("welcome to",self.n)
                self.n=self.model
                break
            elif self.n=="mercedes":
                print("welcome to",self.n)
                self.model()
                break
            elif self.n=="tata":
                print("welcome to",self.n)
                self.model()
                break
            else:
                print("enter valid company")
                break
    def model(self):
        if self.n=="tayota":
            while True: 
                print("enter from odi,creta,eco")
                self.choice=input("select from odi,creta,ecco")
                if self.choice=="odi":
                    self.price(self.choice)
                    break
                elif self.choice=="creta":
                    self.price(self.choice)
                    break
                elif self.choice=="eco":
                    self.price(self.choice)
                    break
                else:
                    print("enter a valid choice")
                    break
        if self.n=="mercedes":
            while True: 
                print("enter from odi,creta,eco")
                self.choice=input("select from odi,creta,ecco")
                if self.choice=="odi":
                    self.price(self.choice)
                    break
                elif self.choice=="creta":
                    self.price(self.choice)
                    break
                elif self.choice=="eco":
                    self.price(self.choice)
                    break
                else:
                    print("enter a valid choice")
                    break
        if self.n=="tata":
            while True: 
                print("enter from odi,creta,eco:")
                self.choice=input("select from odi,creta,ecco")
                if self.choice=="odi":
                    self.price(self.choice)
                    break
                elif self.choice=="creta":
                    self.price(self.choice)
                    break
                elif self.choice=="eco":
                    self.price(self.choice)
                    break
                else:
                    print("enter a valid choice")
                    break
    def price(self,choice):
            if self.choice=="odi":
                self.p=450000
            elif self.choice=="creta":
                self.p=5400000
            elif self.choice=="eco":
                self.p=8900000
            else:
                print("enter a valid choice")
            totalprice=self.p+self.sgst+self.cgst+self.insurance
            print(totalprice)
car=carshowroom()
car.company()
