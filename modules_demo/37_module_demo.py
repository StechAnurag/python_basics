# MODULES in python

import utility

print(utility) # prints the file path to the imported module

print(utility.multiply(2, 3))


# everytime we make a new import our CPYTHON interpreter compiles and caches it in __paycache__ directory.
# next time it serves from cache rather than refering to the module and recompiling it
# if the module gets modified then only, it recompiles and cache it


