#1.namedtuple()Like dictionaries they contain keys that are hashed to a particular valu
import collections
student = collections.namedtuple('student',['name', 'age','rollno'])
s= student("abc", '12','23')

#acces using index age
print(s[1])

#acess using name
print(s.name)

#acess using getattr
print(getattr(s,'rollno'))


#2. dequeue()double-ended)-queue: for memory efficient appends and pops from either side
from collections import deque
d= deque('abc')  # new queue created
for element in d:
    print(element.upper())

#append add at last x
d.append('x')

d.appendleft('o')

#remove and return an element
d.pop()
d.popleft()

#make list of all content of queue
list(d)

#peek at leftmost
print(d[0])

#peek at rightmost
print(d[-1])

#reverse the list
list(reversed(d))

#search element in queue
'a' in d

#add multiple elements to queue
d.extend('mng')



#extend left
d.extendleft('abc')

#right rotation
d.rotate(1)
print(d)

#left rotation
d.rotate(-1)
print(d)

#clear queue
d.clear()


print("3 Counter")
#3.Coounter dict subclass for counting hashable objects
from collections import Counter
c= Counter(a=4,b=2,c=0,d=-2)
#elements()Return an iterator over elements repeating each as many times as its count
print(sorted(c.elements() ))

#most_common([n])Return a list of the n most common elements and their counts from the most common to the least
print(sorted(c.most_common() ))

#subtract([iterable-or-mapping])Elements are subtracted from an iterable or from another mapping
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
