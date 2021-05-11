#Sring Manipulation
''' Strings are iterable '''
myString = 'Blur is Rad'
print(myString[0],myString[1],myString[2])
#methods , change case
print(myString.upper())
print(myString.lower())

#Sentence Methods
sentence = 'my name is Alake Oluwatunmise.i am also known as RAD.rad loves coding '
print(sentence.capitalize())

#Format
year_born = '1922'

print('I was born in {}.'.format(year_born))
#Alternative option to the previous 
print('I was born in' , year_born) 

#Another Example for Format
yearFounded = "1776"
nation = "The US of A"
print("{} was founded in the year {}." .format(nation,yearFounded))

#Split
aString = "I like apples! I like pinapples"
print(aString.split("!"))

#Join
kimiNoNawa = "Taki Kun"
join_result = '_'.join(kimiNoNawa) #that underscore passed in thee method looks like an emoji(^_^)
listOfLaptops =['HP Omen','Macbook','Dell','IBM',]
oneString = '~'.join(listOfLaptops)
print(oneString)

#replace

