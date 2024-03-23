a=int(input("enter your marks in m1: "))
b=int(input("enter your marks in m2: "))
c=int(input("enter your marks in m3: "))
if a>=80 and b>=80 and c>=80:
    print("A+")
elif 60<a<80 and 60<b<80 and 60<c<80:
    print("B+")
else:
    print("fail")