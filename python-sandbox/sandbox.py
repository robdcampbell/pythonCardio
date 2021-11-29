# print('Hello World')

# //////////////////////////////////////////////////////
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

# //////////////////////////////////////////////////////
# Basic While Loop:
            # n = 5
            # while n > 0:
            #     print(n)
            #     n= n-1
            # print('Blastoff!')

# //////////////////////////////////////////////////////
# Basic for loop

def myLoop(x):
        for val in x:
                print(val)

# myLoop('Hello World')
# myLoop([5,4,3,2,1,"BLASTOFF!!!"])

# //////////////////////////////////////////////////////
# try...except   (good for error detection, preventing the rest of code from stopping)
                # greeting = "Welcome"

                # try: 
                #         istr = int(greeting)
                # except: 
                #         istr = -1

                # print("First", istr)

                # astr = "123"
                # try: 
                #         istr = int(astr)
                # except: 
                #         istr = -1
                # print("Second", istr)

# Check data type
        # x = "Hello World"
        # print(type(x))  # str


# //////////////////////////////////////////////////////
# FUNCTIONS /////////////////////////////

def thing(x):
        print("hello")
        print("world")
        print(x)

# thing('Rob')


# ////////////////////////////////////////////////////
# EXAMPLE OF LOOPING A LIST //////////////////////////////////
my_list = ["carrots","corn","broccoli","rice","hummus"]
word = "Hello"
def print_my_list(val):
        count = 0
        for x in val:
                print(count, val[count]) 
                count = count+1
        print('DONE')

# print(my_list[0])

# print_my_list(my_list) #loop through a list
# print_my_list(word) #loop through a string


# ////////////////////////////////////////////////////
# EXAMPLE OF LOOP //////////////////////////////////
def loop_stuff(x):
        count = 0
        for val in x:
                print("Index: ", count, " - ", val)
                count = count +1

# print(loop_stuff(my_list))


# ////////////////////////////////////////////////////
# STRING METHODS //////////////////////////////////
# https://docs.python.org/3/library/stdtypes.html#string-methods

# string[0:2]
# string.lower()
# string.upper()
# string.lstrip()
# string.rstrip()
# string.strip()
# string.startswith()
# string.find( searchTarget, startPosition)



# Slicing strings
# Example 1:
# s = "Monty Python"
        # print(s[0:4])   # start at 0, go to BUT DO NOT INCLUDE 4
        # print(s[6:7])
        # print(s[6:20])

# Slicing can also be applied to lists
        # nums = [4,5,6,7,8,9,12,5645]
        # print(nums[0:2])


# Search and replace 
        # greet = "Hello Bob"
        # nstr = greet.replace("Bob", "Jane")
        # print(nstr)
        # nstr = greet.replace("o", "X")
        # print(nstr)

# Strip whitespace
        # greet = "   Hello Bob   "
        # print(greet.lstrip())
        # print(greet.rstrip())
        # print(greet.strip())


# ////////////////////////////////////////////////////
# READING FILES //////////////////////////////////

# 3:27:50 https://www.youtube.com/watch?v=8DvywoWv6fI