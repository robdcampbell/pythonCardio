# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# String Formatting

#print ('Hello, my name is ' + name + ' I am '+ str(age))

# Arguments by position 
#print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
#print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize())
'''
.upper()
.lower()
.swapcase()
.len() - Length
.replace() - s.replace('world', 'everyone')
.count  -  sub = h  print(s.count(sub))
.startswith()  - s.startswith('hello')
.endswith()
.split()  - will split into a list/array
.find()  -  will find a position of a character
.isalnum  - Is alphanumeric (returns True/False)
.isalpha -  Is alphabetic (returns True/Fals)
.isnumeric  - Is numeric  (returns True/False)


'''

