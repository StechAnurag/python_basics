# List Unpacking

a,b,c = [1, 2, 5]

print(a)
print(b)
print(c)

# x,y,z = [3, 4, 5, 7, 8, 9] # ERROR: num of items to unpack must be equal

x,y,z, *others = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print(x)
print(y)
print(z)
print(others)

i,j, *unuseds, k = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(i)
print(j)
print(k)
print(unuseds)
