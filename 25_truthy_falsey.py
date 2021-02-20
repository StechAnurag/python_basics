# TRUTHY & FALSEY

# A Truthy value is that on which if we apply a bool(value) type conversion, then it evaluates to  - True
name = 'Salman'
age = 38

print(bool(name))
print(bool(age))

# A Falsey value is that on which if we apply a bool(value) type conversion, then it evaluates to  - False
name = ''
age = 0
print(bool(name))
print(bool(age))

# Reference - https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false