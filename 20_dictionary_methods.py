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