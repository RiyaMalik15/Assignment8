print("Question1")
#We represent time in a way that’s easy for us to understand
#However, Python stores it in tuples.
#These python tuples are made of nine numbers.
#Index	Field	            Domain of Values
#0	Year (4 digits)	        Ex.- 1995
#1	Month	                1 to 12
#2	Day	                1 to 31
#3	Hour	                0 to 23
#4	Minute	                0 to 59
#5	Second	                0 to 61 (60/61 are leap seconds)
#6	Day of Week	        0 to 6 (Monday to Sunday)
#7	Day of Year	        1 to 366 (Julian day)
#8	DST	                -1,0,1
print('*'*10)
print('\n')

print("Question2")
import datetime
time=datetime.datetime.now()
print(time.strftime("%Y %b %d %H:%M:%S"))
print('*'*10)
print('\n')

print("Question3")
import datetime
time=datetime.datetime.now()
print(time.strftime("%B "))
print('*'*10)
print('\n')

print("Question4")
import datetime
time=datetime.datetime.now()
print(time.strftime("%A "))
print('*'*10)
print('\n')

print("Question5")
import datetime
d=datetime.datetime(2010,9,6,19,30)
print(d.day)
print('*'*10)
print('\n')

print("Question6")
import time
print("Localtime:",time.localtime(time.time()))
print('*'*10)
print('\n')

print("Question7")
import math
n=int(input("Enter number"))
print("Factorial:",math.factorial(n))
print('*'*10)
print('\n')

print("Question8")
import math
x=int(input("Enter first number"))
y=int(input("Enter second number"))
print("Greatest common divisor:",math.gcd(x,y))
print('*'*10)
print('\n')

print("Question9")
import os
print("Current Working Directory:",os.getcwd())
print("User Environment:",os.environ)
print('*'*10)
