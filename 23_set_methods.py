# Set Methods

my_set = {1, 2, 3, 4, 5}
your_set = {2, 4, 6, 8, 10}


# difference
print(my_set.difference(your_set))

# discard - removes/deletes an item
#print(my_set.discard(5))
print(my_set.discard(6)) # removing a non-existent does not throw error

# difference_update - removes the common items from my_set
#print(my_set.difference_update(your_set))
print(my_set)

# intersection - the common elements
print(my_set.intersection(your_set))
print(my_set & your_set) # just a shorthand for intersection operation

# isdisjoint - checks if the sets do have something in common
print(my_set.isdisjoint(your_set))

# union
print(my_set.union(your_set))
print(my_set | your_set) # just a shorthand for union operation

# issubset - checks if the set is subset of other
print(my_set.issubset(your_set))

# issuperset - checks if the set is superset of the other
print(my_set.issuperset(your_set))



#Referernce - https://www.w3schools.com/python/python_ref_set.asp