# DICTIONARY KEYS

# - A dictionary key must be immutable
dictionary = {
  '123': 123,
  True: 'hello',
  2020: [12, 21, 31]
  #[10,20]: 'some value' // ERROR
}

print(dictionary)

# - A dictionary key must be unique, otherwise its value gets overwritten

a_dictionary = {
  '123': 'cool',
  '123': 'hot'
}

print(a_dictionary)