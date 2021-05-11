# This python file is for you to practice your scripts and see examples of how code works
import math

print ('This code doesnot affect  the program') 
l = 2
w = 3
d = math.sqrt(l**2 + w**2) #length of a diagonal

#Comments should be used sparingly
print (d)

for i in range (2):
    print ('Hello, World')

for i in range (2):
    print (d)    

print ('''Tunmise is my name
and this is my first multiline line statement''')


country = 'Nigeria'
if country == "Nigeria":
    print ('Hello',country)
else:
    print ('Hello Foreign Land')

#---------------------------------------------------
x = 10
y = 11

#nested if-else statements

a  = 2
if a==2:
    print('The Number is 2')
if a%2 == 0:
    print('The number is even')
if a%2 != 0:
    print('The number is not even')
#--------------------------------------
if x == 10:
    if y == 11:
        print(x+y)
    else:
        print(x)
else:
    print('Cannot run')
#----------------------------------------------------

  




