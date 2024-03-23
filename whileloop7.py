n=153
s=0
a=n
while n>0:
    n=n//10
    d=n%10
    d=n**3
    s=s+d
print(s)
if s==a:
    print("yes")
else:
    print("no")
