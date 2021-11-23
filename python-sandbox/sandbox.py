# print('Hello World')


# Basic Conditional Code:
    # ex 1
            # x = 10
            # if x < 8:
            #     print("Smaller than 8")
            # elif x > 8:
            #     print("Greater than 8")
    # ex 2
            # y = 4

            # if y >2:
            #     print('Bigger')
            # else:
            #     print("Smaller")
            # print("all done")

# Basic While Loop:
            # n = 5
            # while n > 0:
            #     print(n)
            #     n= n-1
            # print('Blastoff!')

# Basic for loop


# try...except   (good for error detection, preventing the rest of code from stopping)
greeting = "Welcome"

try: 
        istr = int(greeting)
except: 
        istr = -1

print("First", istr)

astr = "123"
try: 
        istr = int(astr)
except: 
        istr = -1
print("Second", istr)

# Check data type

x = "Hello World"
# print(type(x))  # str

# //////////////////////////////////////////////////////
# FUNCTIONS

def thing(x):
        print("hello")
        print("world")
        print(x)

# thing('Rob')

my_list = ["carrots","corn","broccoli","rice","hummus"]
word = "Hello"
def print_my_list(val):
        count = 0
        for x in val:
                print(count, val[count]) 
                count = count+1
        print('DONE')

print(my_list[0])

print_my_list(my_list) #loop through a list
# print_my_list(word) #loop through a string

