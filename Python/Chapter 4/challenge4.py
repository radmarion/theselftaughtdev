a = 3
b = 4
def doSomething (x,y):
    x = x + a
    print(x+y)


if (a<=10):
    print(doSomething(3,6),b)
else:
    print('not working')

doSomething(9,10)

for i in range (10):
    print(doSomething(2,3),i)
# What does the output of the case mean