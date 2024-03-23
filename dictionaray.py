d={21:"siva",
    22:"ram",
    23:"charan",
    24:"vikram",
    "siva":104
}
print(d)
d[21]="konidela"
print(d)
d[25]="klin"
print(d)
for i in d:
    print(i)
for i in d.values():
    print(i)
for x,y in d.items():
    print(x,y)
d.pop(21)
print(d)

