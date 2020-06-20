#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets
tup=('priya','surabhi','zia')
print(tup)

#acessing tuple is same as list
print(tup[0])
print(tup[-1])
print(tup[0:1])
print(tup[-2])


#Iterate through the items and print the values:
for item in tup:
    print(item)

#Add Items
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
#tup[2]='xxx'

#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
del tup

#To join two or more tuples you can use the + operator:
t1=('a','b')
t2=('v','y','z')
t3=t1+t2
print(t3)
