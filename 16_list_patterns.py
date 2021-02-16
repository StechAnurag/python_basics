# Common List Patterns

basket = ['Apple', 'Guava', 'Banana', 'Lichi']

#1) length
print(len(basket))

#2) sorting
basket.sort()
print(basket)

#3) Reversing
basket.reverse()
print(basket)

#4) copying a list / portion of a list
print(basket[:])

#5) Joining list items
new_sentence = ' '.join(basket)
print(new_sentence)

#6) creating a list quickly with range(start, stop)
numbers = list(range(1, 100))
print(numbers)

whole_numbers = list(range(100))
print(whole_numbers)