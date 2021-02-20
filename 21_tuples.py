# TUPLE : tuples are immutable lists. the items of a tuple cannot be changed once after declaration.
# -- they are much perfomant

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)

print(my_tuple[0])

# my_tuple[0] = 12 # ERROR

user = {
  'name': 'Rahul',
  'age': 45,
  'cities': ['New Delhi', 'Pensilvenia', 'Singapore', 'Amethi']
}

print(user.items()) # prints in tuple format

# So, dictionary key can be valid tuple

user2 = {
  'name': 'Parul',
  'age': 54,
  (1, 2): ['New Delhi', 'Pensilvenia', 'Singapore', 'Amethi']
}

print(user2) #tuple (1,2) is valid key for the dictionary


# Tuple slicing
new_tuple = my_tuple[1:4]
print(new_tuple)

# Tuple unpacking
a, b, c, *others = my_tuple;
print(a)
print(b)
print(c)
print(others)

# Tuple Methods
print(my_tuple.count(3)) # counts the occurance
print(my_tuple.index(2)) # finds the index of an item
