# *args , **kwargs

def func(*args, **kwargs):
  print(args) # the function receives *args as a tuple
  print(kwargs) # the function receives **kwargs as dict
  total = 0
  for item in kwargs.values():
    total += item
  return sum(args) + total

print(func(1,2,3,4, apple=10, orange=15))


# Rule: params, *args, default_params, **kwargs