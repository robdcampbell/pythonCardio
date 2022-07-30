# BASIC CRASH COURSE. print("hello, world.")

### Declaring variables: 
my_first_variable = 'Python'

### Commenting : you comment in python using the "#" sign

# normal comment 

"""
    this is a multi-line comment
"""


### casting to other data types:
a = str(3)    # x will be '3'
b = int(3)    # y will be 3
c = float(3)  # z will be 3.0
    # getting a type:
# print(type(a))
# print(type(b))


### Unpacking a collection / similar to destructuring in other languages

fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
#   print(x)
#   print(y)
#   print(z)

########################################################
### DATATYPES

# TEXT:     str
# NUMERIC:  int, float, complex 
# SEQUENCE: list, tuple, range 
# MAPPING:  dict 
# SET:      set, frozenset 
# BOOLEAN:  bool 
# BINARY:   bytes, bytearray, memoryview 
# NONE:     NoneType 

# get a data type: type()
#   print(type("Hello World"))  # will print: <class 'str'>

### NUMBERS: 
num1 = 1    # int
num2 = 2.8  # float
num3 = 1j   # complex
# print(type(num1)) # <class 'int'>
# print(type(num2)) # <class 'float'>
# print(type(num3)) # <class 'complex'>


#### STRINGS

# Loop through characters in an string
for val in "Hello World":
    val
    # print("letter: " + val)

# String length
strExample = "Hello, World!"
# print(len(strExample))
# print(strExample[0])
# print(strExample[0:3])
# print(strExample[1:])       # slice to the end of the str
# print(strExample[-6:-1])    # negative indexing
# print(strExample)           # not mutated

# Slicing strings: 
b = "Hello, World!"
# print(b[2:5])

# Iteration number in for-loop Python
a_list = ["a", "b", "c", "d"]

# for iteration, item in enumerate(a_list):
#   print(iteration)

count = 0
for x in a_list:
        print(count)
        count = count+1


### Checking for presence of a str within a string
txt = "The best things in life are free!"
print("free" in txt) # returns true
print("3.50" in txt) # returns false