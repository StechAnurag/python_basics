# UNIQ PYTHON string manipulation

some_str = 'Apple Banana Orange'

print(some_str[0])

# [start:stop]
print(some_str[0:5])

# without end -- it goes all the way to end to the string
print(some_str[0:])

# without start -- it starts with the 0 index
print(some_str[:12])

# without start, without end -- [0:lenghtOfstr] default behavoir
print(some_str[:])

# [start:stop:stepover]
print(some_str[1::3])

# traversing from end -- print the 2nd character from the end
print(some_str[-2])

# reverse a string
print(some_str[::-1])

print(some_str[-1:-15:-1])