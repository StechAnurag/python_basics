# LIST SLICING : works similar to string slicing

amazon_cart = [
  'notebook',
  'sunglasses',
  'jeans',
  'backpack'
]

print(amazon_cart)

print(amazon_cart[0:3])

# with stepover
print(amazon_cart[1::2])

# We can mutate a list i.e., we can replace a list item
amazon_cart[2] = 'toys'
print(amazon_cart)

# List slicing returns a new copy of the list
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)

# Lists are reference types i.e., 
flip_cart = amazon_cart
flip_cart[0] = 'Pinapple'
print(flip_cart) 
print(amazon_cart) # both point to the same memory location, so actually mutate the original list

# making a copy of the list
snapdeal_cart = amazon_cart[:]
snapdeal_cart[0] = 'Carpet'
print(snapdeal_cart) 
print(amazon_cart)
 
