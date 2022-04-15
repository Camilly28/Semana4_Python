
x = int(input())
verdade = 'false'
while verdade =='false':
  y = int(input())
  if x > y:
    print('menor')  
  if x < y: 
    print('maior')
  if x == y:
    print('igual')
    verdade = 'verdade'
