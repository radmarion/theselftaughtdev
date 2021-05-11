#SCOPE  : refers to what part of your code can access the variable




# Global Variables : Can be Accessed anywhere in a code
a = 1
b = 2 
c = 3
print(a,b,c)

def q():
    print(a,b,c)
q()

# Non - Global Vairiables
def y():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)

# Using Global Variables in functions
x = 1001

def y():
    global x
    x+=1
    print(x)
y()

print(type(y))

rad = "Tunmise"
print(len(rad))

daft = 'Tomisona Alake'
