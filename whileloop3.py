# n=12345
# s=0
# while n>0:
#     a=n%10
#     s=s+a
#     n=n//10
# print(s)




def f(n):
    if n<10:
        return n
    else:
        return n%10+f(n//10)
a=f(23)
print(a)


        
    