# FUNCTIONS

def say_hello():
  print('Hello India')


say_hello()
say_hello()
say_hello()


# with parameters
def greet(name, emoji):
  print(f'Hello {name}{emoji}')

# Positional Arguments
greet('Alan', '😊')
greet('Emilly', '😊')
greet('Robot', '😊')


# Keyword Arguments : by the use of this we can change the calling positions of arguments
greet(emoji='😊', name='James')


# with default parameters
def greet1(name = 'Alan Walker', emoji='🐻'):
  print(f'Hello {name}{emoji}')

greet1()
greet1('Billy Ellish')

# With Return
def sum(num1, num2):
  return num1 + num2

print(5+9)

# BEST PRACTICES
# -- A function should do one job really well
# -- A function should return something

