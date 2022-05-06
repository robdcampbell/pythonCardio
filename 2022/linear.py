# print("Linear Search up in here")

def linear_search(list, target): 
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index )
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result1 = linear_search(numbers,12)
result2 = linear_search(numbers,9)

# print(linear_search(numbers,9))

verify(result1)
verify(result2)