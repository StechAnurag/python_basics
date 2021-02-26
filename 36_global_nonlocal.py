# GLOBAL keyword


total = 0;

def count():
  global total
  total += 1
  return total

count()
count()
print(count())

# Better way of doing this is - dependency injection

def counter(total):
  total += 1
  return total

print(counter(counter(counter(1))))

# NONLOCAL keyword

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

# [MOST IMP]: - A child can have access to its parent / global scope, though it can't modify a parent/global variable
# unless it explicitly referenced with a global or nonlocal keyword