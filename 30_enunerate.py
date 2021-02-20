# Enumerate - produces an enumerable iterable from an iterable

for i,char in enumerate('Helllooo'):
  print(i, char)


# with lists
for i, v in enumerate([1, 2, 3]):
  print(i, v)


# with tuples
for i, v in enumerate((1, 2, 3)):
  print(i, v)

for ind, val in enumerate(list(range(100))):
  print(ind, val)
  if val == 50:
    print(f'index of {ind} is {val}')