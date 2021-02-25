# DOCSTRINGS - are used to document the action within a function

def test(a):
  '''
  Info: this function tests and prints param a
  '''
  print(a)



# to read documenation there are 3 ways
# 1 - our text editor helps with it
# 2 - help function
# 3 - .__doc__  dundar method

print(help(test))

print(test.__doc__)