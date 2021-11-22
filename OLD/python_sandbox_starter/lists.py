# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list 
    #numbers = [1,2,3,4,5]
fruits=['Apples', 'Oranges', 'Grapes', 'Pears']
# Use a constructor (NOT USED NORMALLY)
numbers2 = list((1,2,3,4,5))

# Get Values
    #print(fruits[2])

# Get Length 
    #print(len(fruits))

# Append to list 
fruits.append('Mangoes')
    #print(fruits)

# Remove from List
fruits.remove('Grapes')

# Insert into Position
fruits.insert(2, "Strawberries")

# Change Value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse the list 
fruits.reverse()

# Sort list 
fruits.sort()

# Reverse sort 
fruits.sort(reverse=True)

print(fruits)

