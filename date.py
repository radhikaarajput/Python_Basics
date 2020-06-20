#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime
from datetime import date

a = datetime.datetime.now()  #date contains year, month, day, hour, minute, second, and microsecond
print(a)
print(a.year)

#The datetime object has a method for formatting date objects into readable strings.
#The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

print(a.strftime('%B'))   #format %B month


# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#We can also create date objects from a timestamp. 
# A Unix timestamp is the number of seconds between a particular date and January 1, 1970 at UTC.
# You can convert a timestamp to date using fromtimestamp() method.
timestamp = date.fromtimestamp(1324364)
print("Date =", timestamp)