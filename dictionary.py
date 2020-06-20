#A dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

dict={'name':'ram' ,'id':'a12', "year":4590}
print(dict)

#You can access the items of a dictionary by referring to its key name, inside square brackets:
print(dict['id'])
#get() that will give you the same result
a=dict.get('name')
print(a)

#change the value of a specific item by referring to its key name
dict['name']='siya'
print(dict)

#looping through a dictionary, the return value are the keys of the dictionary
for item in dict:
    print(item)

#Print all values in the dictionary, one by one
for item in dict:
    print(dict[item])

#or use values for this
for item in dict.values():
    print(item)


#Loop through both keys and values, by using the items() method:
for x,y in dict.items():
    print(x,y)

#To determine if a specified key is present in a dictionary use the in keyword:
if 'name' in dict:
    print('Yes name exist')

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
dict['marks']=89
print(dict)

#pop() method removes the item with the specified key name
dict.pop('id')
print(dict)

#popitem() method removes the last inserted item
dict.popitem()
print(dict)

#del keyword removes the item with the specified key name
del dict['name']
print(dict)

#copy, one way is to use the built-in Dictionary method co
mydic= dict.copy
print(mydic)

#A dictionary can also contain many dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)