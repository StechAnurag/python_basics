# CONCEPT: STRINGS ARE IMMUTABLE in pyhton

fruit = 'Apple'
print(fruit)

# we can reassign a whpole new value to fruit
fruit = 'Orange'
print(fruit)
# but we can't replace any character of the string
# strings are immutable
#fruit[0] = 'U' # ERROR
# print(fruit)


quote = 'To be or Not to be'
# we're just overriding the value of quote in memory
print(quote.replace('be', 'me'));
# but we can save it in other variable
quote2 = quote.replace('be', 'me')

# but the quote remains original, immutable
print(quote)

print(quote2)
