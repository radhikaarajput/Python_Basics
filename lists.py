#A list is a collection which is ordered and changeable. In Python lists are written with square brackets

l1=['abc','app','hey']
print(l1)

#access the list items by referring to the index number:
print(l1[1])

#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc
print(l1[-1])

#specify a range of indexes by specifying where to start and where to end the range
print(l1[1:2])

#By leaving out the end value, the range will go on to the end of the list
print(l1[1:])

#Specify negative indexes if you want to start the search from the end of the list
print(l1[-2:-1])

#o change the value of a specific item, refer to the index number
l1[1]='soft'
print(l1)

#loop through the list items by using a for loop:
for item in l1:
    print(item)

#determine if a specified item is present in a list use the in keyword:
if 'soft' in l1:
    print("Soft present in List l1")

#determine how many items a list has, use the len() function:
print(len(l1))

#add an item to the end of the list, use the append()
l1.append('priya')
print(l1)

#Insert an item as the second position
l1.insert(2,'surabhi')
print(l1)

#remove() method removes the specified item
l1.remove('soft')
print(l1)

#The pop() method removes the specified index, (or the last item if index is not specified):
l1.pop()
print(l1)

l1.pop(0)
print(l1)

#del keyword removes the specified index
del l1[0]
print(l1)

#The del keyword can also delete the list completely: del l1

#clear() method empties the list : l1.clear()

#Make a copy of a list with the copy() method
l2= l1.copy()
print(l2)

#Join Two Lists
l3=l1+l2
print(l3)

#Another way to join two lists are by appending all the items from list2 into list1, one by one
l1.append(l2)
print(l1)

#se the extend() method, which purpose is to add elements from one list to another list
l1.extend(l2)
print(l1)
