# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples, Oranges', 'Grapes'))

#print(fruits, fruits2)

# Get Value
    #print(fruits[1])

# Can't change value
    # fruits[0] = "Pears" -> Will throw an error

# Delete Tuple
    # del fruits2

# Get Length
# print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {'Apples', 'Oranges', 'Mango'}

#print('Apples' in fruits_set)

# Add to set 
fruits_set.add('Grape')

# Add duplicate
fruits_set.add('Apples')

# Remove from set 
#fruits_set.remove('Grape')

# Clear Set
#fruits_set.clear()

print(fruits_set)