n=47
s=0
a=n
while n>0:
    d=n%10
    s=s+d
    n=n//10
if a%s==0:
    print("divisible")
else:
    print("not divisible")
