#The try clause can be used like an if-elses statement in handling exceptions


a = input('type a number  ')
b = input('type another number  ')
a = int(a)
b = int(b)

try:
    print(a/b)
    print(int(a/b))
except ZeroDivisionError:
    print('b cannot be zero. Try again')
except SyntaxError:
    print("Number is supposed to be an integer")