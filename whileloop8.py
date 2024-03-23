n=153
nod=0
n1=n
org=n
while n>0:
    n=n//10
    nod=nod+1
sum1=0    
while n1>0:
    d=n1%10
    sum1=sum1+d**nod
    n1=n1//10
print(org)
if sum1==org:
    print("yes")
else:
    print("no")