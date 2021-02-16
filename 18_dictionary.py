# DICTIONARY / dict -- it's a data type also a data structure in pyhton. A dictionary is a collection of unordered key value pairs.

dictionary = {
  'a': 1,
  'b': 2,
  'c': 3
}

print(dictionary)
print(dictionary['a'])
# unordered means that items are not right next to each other in memory.

# List of dictionaries
my_list = [
  {
    'a': 'cool',
    'status': True,
    'params': [12, 24, 36]
  },
  {
    'a': 'hot',
    'status': False,
    'params': [6, 24, 96]
  }
]
print(my_list)
print(my_list[0]['a'])


