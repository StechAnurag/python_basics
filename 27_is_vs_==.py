# is VS ==


# Implicit type conversion takes place wherever possible
print(True == 1)
print('' == 1)
print(10 == 10.0)
print([] == [])
print('1' == 1)
print([] == 1)
# == checks if the two values are equal


# is - checks the exact reference of the values in memory
print(True is True)
print('1' is 1)
print([1,2,3] is [1,2,3])