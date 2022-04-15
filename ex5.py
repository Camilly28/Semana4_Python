nome = input()
nome_soletrado = ""
while True:
  letra = str(input())
  if letra == '.':
    break
  nome_soletrado += letra
if nome_soletrado == nome:
  print('True')
else:
  print('False')

