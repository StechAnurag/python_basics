#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

heart = [
  [0,0,0,0,0,0,0],
  [0,1,1,0,1,1,0],
  [1,0,0,1,0,0,1],
  [0,1,0,0,0,1,0],
  [0,0,1,0,1,0,0],
  [0,0,0,1,0,0,0]
]

for item in picture:
  for sub_item in item:
    if(sub_item == 0):
      print(' ', end =' ')
    else:
      print('*', end =' ')
  print('')

for image in heart:
  for pixel in image:
    if(pixel == 0):
      print(' ', end =' ')
    else:
      print('*', end =' ')
  print('')