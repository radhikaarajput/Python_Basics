print("Exception handling for input **user can enter a number only")
while True:
    try:
        x=int(input("Enter Number: "))
        break
    except ValueError:
        print("Not a valid Number")

#else keyword to define a block of code to be executed if no errors were raised
print("Exception handling use of else keyword")
try:
    print("In try")
except:
    print("Something went wrong")
else:
    print("ELSE!! Nothing went wrong")

# finally is used to execute clean up actions and excetued always
print("close file with finally block")
try:
    f=open("my.txt")
    f.write("Hey!!")
except:
    print("Some exception occur")
finally:
    f.close();

#Raise As a Python developer you can choose to throw an exception if a condition occurs
print("raise if x!=0")
x=-1
if x==0:
    raise Exception("X should be equal to 0")

#Raise a TypeError if x is not an integer
print("Raise a TypeError if x is not an integer")
x="abc"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

