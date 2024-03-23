a=int(input("enter a value a : "))
if a%3==0 and a%5==0:
    print("GREAT")
elif a%3==0 and a%9==0:
    print("GOOD")
elif a%3==0 and a%7==0:
    print("OK")
else:
    print("NOT GOOD")