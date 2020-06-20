#set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
set1={'a','b','c'}
print(set1)      #Sets are unordered, so you cannot be sure in which order the items will appear.

#specified value is present in a set, by using the in keyword.
for item in set1:
    print(item)

#To add one item to a set use the add() method
set1.add('red')

#Add multiple items to a set, using the update() method
set1.update(['wait','xyz','arm'])
print(set1)

#to determine how many items a set has, use the len() method.
print(len(set1))

#To remove an item in a set, use the remove(), or the discard() method
set1.remove('a')
print(set1)

#Remove  by using the discard() method
set1.discard('red')
print(set1)

#Remove the last item by using the pop() method
#using the pop() method, you will not know which item that gets removed
a=set1.pop()
print(a)
print(set1)


#The clear() method empties the set
set1.clear()

#del keyword will delete the set completely
del set1

#union() method that returns a new set containing all items from both sets
s1={1,2,3}
s2={7,30}
s3=s1.union(s2)
print(s3)

#update() method inserts the items in set2 into set1
s1.update(s2)
print(s1)