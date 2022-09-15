# print('pterodactyls')

my_items = {
    "tv": 30,
    "timmy": 20,
    "stereo": 50
    }


def find_it(items, name):
    if name in items.keys():
        print("its here")
    else:
        print("no senor")


find_it(my_items, 'timmy')
find_it(my_items, 'john')


# print(find_it(my_items, "timmy"))
# print(find_it(my_items, "charles"))

##################

# Python3 Program to check whether a
# given key already exists in a dictionary.

def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end=" ")
        print("value =", dic[key])
    else:
        print("Not present")



# Driver Code
dic = {'a': 100, 'b': 200, 'c': 300}
key = 'b'
#checkKey(dic, key)

key = 'w'
#checkKey(dic, key)