input=[1,2,3,4,5]
outlist=[]
for var in input:
    if var%2==0:
        outlist.append(var)


print("Even Numbers: ")
print(outlist)

print("List Items: ")
for i in range(5):
    print(i)

print("List Items: ")
for i in [1,2,3,4,5]:
    print(i)

l= [(var)if (var%2 == 0) else (33 if (var==3) else 0) for var in input]
print(l)

