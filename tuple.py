tuple=("surya","leela","ayyappa","sivabraham",90.8,76,426)
print(tuple)
tuple=tuple+("hello",)
print(tuple)
tuple=tuple+("hello",19,"sai")
print(tuple)
for i in range(0,5):
    n=int(input("enter a number: "))
    tuple=tuple+(n,)
print(tuple)