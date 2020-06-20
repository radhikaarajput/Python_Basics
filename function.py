#count number of digits in a number
def count(n):
    string= str(n)
    length=len(string)
    return(length)

print(count(9))

#global local x
x=5
def gloLocVar():
    x=0
    return x

print(x)
print(gloLocVar())
print(x)

#convert a sentence into upper case
def uppCase(string):
    u=string.upper()
    return u

print(uppCase("heyyy"))

#function to count number of elements in a list
def length_list(l):
    print(l[1])
    print(l[-1]) #last element
    print(l[0:3]) #print 3e first
    print(l[:3])
    return len(l);

length_list([1,2,3,4,5])

#add element at position 2
def ins(ele, pos, list1):
    return list1.insert(pos,ele)

ins(2,0)
print(l)
