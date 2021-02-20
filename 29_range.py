# range()

print(range(1, 100))
print(range(100)) # it prints 0, 100

for i in range(0, 10): # range object is also iterable
  print(i)


# with step over
for _ in range(0, 10, 2):
  print(_)

# iterating in descending order
for _ in range(10, 0, -1):
  print(_)

# creating a list from a range
for _ in range(2):
  print(list(range(10)))