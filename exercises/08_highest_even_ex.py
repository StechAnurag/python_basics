#Q: find the highest even number from a given list

def highest_even(li):
  evens = []
  for el in li:
    if el % 2 == 0:
      evens.append(el)
  return max(evens)
  

print(highest_even([36, 1, 2, 3, 54, 9, 11, 12, 17, 24]))