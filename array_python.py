a=[1,2,3,4,5]

print(a)

#look at single index
print("#look at single index 3")
print(a[-3])

#add new items
print("#add new items 99")
a.append(99)
print(a)

#remove an element
print("#remove 2")
a.remove(2)

#insert in middle of list pos,element value
print("#insert in middle of list pos,element value 4,100")
a.insert(4,100)
print(a)

#remove particular element using index
print("#using pop")
a.pop(1)
print(a)

#replace some item
print("#replace 3 with 400")
a[3]=400
print(a)

#length of list
print("#Length")
print(len(a))

#to know type of list
print("#type is")
print(type(a))

#concatenate 2 lists
print("#conactenation of list")
a=[1,2,3]+[6,7,8]
print(a)