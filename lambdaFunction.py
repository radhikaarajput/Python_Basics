#A lambda function can take any number of arguments, but can only have one expression

#lambda fn adds 10
x= lambda a: a+10
print(x(7))

#A lambda function that multiplies argument a with argument b and print the result:
x=lambda a, b: a*b
print(x(2,3))

#power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def fn(n):
    return lambda a: a*n;

x= fn(3)
print(x(2))