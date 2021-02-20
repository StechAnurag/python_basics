# DICTIONARY METHODS

user = {
  'name' : 'John Doe',
  'is_alien': True,
  #'age': 50 
}

print(user.get('age'))

# accessing a key that does not exit

#print(user['age']) # ERROR
print(user.get('age', 55)) # assigning a default value if it does not exist

player = {
  'name' : 'Virat Kohli',
  'age': 33,
  'level': 'International',
  'sports' : ['cricket', 'Football'] 
}


# Finding an item
print('sports' in player) # returns True - if found / False otherwise

# Finding a key
print('ages' in player.keys())

# Finding a value
print(33 in player.values())

# Print the dictionary items as tuples
print(player.items())

# Remove everything
user.clear()
print(user)

# Copy a dictionary
player2 = player.copy()
print(player2)

# Remove a key
print(player2.pop('age'))
print(player2)

print(player2.popitem()) # it randomly pops off an item

# Update an item
print(player.update({'age': 35}))
print(player.update({'children': 1})) # added an item if does not already exist