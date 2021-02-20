# SETS : Sets are unordered collection of unqiue objects/items

my_set = {1, 2, 3, 4, 5}

print(my_set)

# Adding an item
my_set.add(6)
print(my_set)

my_set.add(5) # adding duplicate value just replaces it in the memory location - it does not get added.
print(my_set)

# Accessing a set item
print(1 in my_set)
#print(my_set[1]) # ERROR

# Length of a set
print(len(my_set))

# Copying a list 
my_set2 = my_set.copy()
print(my_set2)

my_set2.clear()


# Reference - Python Sets https://www.w3schools.com/python/python_ref_set.asp