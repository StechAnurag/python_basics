# List Methods

basket = ['Apple', 'Banana', 'Orange', 'Pineapple', 'grapes']

# counting the length
print(len(basket))

# Adding to list
basket.append('Pomegranate') 
basket.insert(3, 'Lichi') # inserts at a certain index
basket.extend(['Mango', 'Coconut']) # appends / concatenates another list at the end
print(basket)

# Removing from list
basket.pop()
print(basket)
basket.pop(2) # removing from a specific index
print(basket)
basket.remove('Lichi') # removing an item with its name/value
print(basket)
basket.clear() # removes everything from a list
print(basket)

# Count the occurance of an item
buildings = ['a', 'b', 'd', 'd', 'e', 'x', 'h', 'f']
print(buildings.count('d')) 

# Finding an item in the list
print(buildings.index('e'))
#print(buildings.index('k')) # if the element does not exist, then it throws an error
# -- alternative approach
print('k' in buildings)
print('h' in buildings)

# Sorting
buildings.sort() # it returns none, but mutates the original list
print(buildings)
gardens = ['n', 'o', 'm', 'r']
print(sorted(gardens)) # sorted() functions returns a new_copy of sorted list, it doesn't modifies the actual list
print(gardens)

# Copying a list
new_gardens = gardens.copy()
print(new_gardens)

# Reversing the order of items
new_gardens.reverse()
print(new_gardens)