#SCOPE - what variables do I have access to?

# In python there is functional scope - i.e., there is only a way to
# create a new scope is to create a function.
# There is no any concept of block scope

if True:
  z = 10

def sayHi():
  total = 100

print(z) # it has access to
#print(total) # it does not have access


# Scope Rules: How pyhton interpreter looks for a varible

# 1 - start with local scope
# 2 - check in parent local
# 3 - check in global scope
# 4 - check if built in pyhton variable/function


# [MOST IMP]: - A child can have access to its parent / global scope, though it can't modify a parent/global variable

a = 1

def parent():
  def confusion():
    return a
  return confusion()

print(a)
print(parent())