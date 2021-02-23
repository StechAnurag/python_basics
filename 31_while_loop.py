# WHILE LOOP

i = 0
while i < 20:
  print(i)
  i += 1


# with else block
j = 0
while j < 10:
  print(j)
  j += 1
  if i == 5:
    break
else:
  print('done with loop')

# Note: else block not gets executed if the loop is terminated by a break - It only gets executed when the loop finishes its all iterations and was not exited by a break

