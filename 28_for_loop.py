# FOR Loop

# Iterables in python - Lists, Tuples, Sets, Dictionary, Strings

for item in 'Zero to mastery':
  print(item)

# with lists
for el in [1, 2, 3, 4, 5]:
  print(el)

# with sets
for el in {1, 2, 3, 4}:
  print(el)

# with tuples
for i in (1, 2, 4):
  print(i)

# Nested for loops
for item in [1, 2, 3]:
  for el in ['x', 'y', 'z']:
    print(item, el)


# with dict
bird = {
  'name' : 'Swan',
  'can_fly': True,
  'can_swim': True,
  'avg_weight': 2.5
}

for item in bird:
  print(item) # prints the keys not values

for item in bird.items():
  print(item) # prints a tuple of (key,value)

# improved version of above
for item in bird.items():
  key,value = item # tuple unpacking
  print(key,value)

# Shorthand vesrsion of above
for key, value in bird.items():
  print(key, value)

for item in bird.values():
  print(item) # prints value

for item in bird.keys():
  print(item) # prints the keys
