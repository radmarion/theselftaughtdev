#Can't be changed, once created, re4peresented with parenthesis
my_tuple = ()#***** check line 12
print(type(my_tuple))
 # or 
this_tuple = tuple()
print(type(this_tuple))
my_tuple = ("red","brown","wings")
print(my_tuple)
#A tuple with one item in it still needs a comma after the item , not applicable to python 3.8
my_tuple = ('self_taught',)
print(my_tuple)
this_tuple = tuple('Rad',) #Only recieves one argument and tuples the inside , same with the list() function
this_tuple = ('rad', 'Fadilah','agunbiade','Stuff')
# you can still acces stuff inside a tuple like a list
print(this_tuple)
aword = this_tuple[2]
print(aword)
names = this_tuple[1:4]
print(names)