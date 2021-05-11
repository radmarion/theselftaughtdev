# Functions can be divided into definition and parameter
# In maths f(x)= x * 6 is a function
# F(x)is the definition and  x  is the parameter i.e the input
#x*6
# Value return Example
c = 5
def f(x):
    return x * 2 ** c
result = f(2)
print(result)

# Statement return example
#https://github.com/calthoff/tstp/blob/master/part_I/functions/df_ex3.py

def even_odd(x):
    if x % 2 == 0:
        print('even')
    else:
        print('odd')
even_odd(2)
even_odd(3)

#functions with empty parameters

def b():
    return 3 + 1
result = b()
print (result)

# function with multiple parameters

def multiple(x,y,z):
    return x + y + z
result = multiple(1,4,5)
print(result)

#instead of using"return" you can use the print statement to sinplify things and avoid too much variable assigning
# For Exmaple:

def bird(e,f):
    print(e+f,"Myname is rad")
bird(3,4)

# Since there was no return statemant , the functions can be called with out being defined

#optional parameters in functions

def e(x=10):
    if x==10:
        print ('x is ten')
    elif x < 5:
        print ('x is less than five')
    else: 
        print('x is not ten')
f(3)
f(11)


# Using both required and optional parameters


def required_optional(x,y=13):
    return x + y
f = required_optional(3,) #required x + optional y
g = required_optional(3,18)
print(f)
print(g)
print(f+g)

#passing functions

def z():
    pass
z()

#Nested Functions

def p():
    print('Inner function')
    def x():
        print('nested function')
    x()
p()






