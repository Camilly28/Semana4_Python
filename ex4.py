pessoa = input()
lista = []

while pessoa != 'fim':
  if pessoa.startswith('0'): 
    pessoa = pessoa.replace('0','')
    lista.append(pessoa)
  
  elif pessoa == '1':
    if len(lista) > 0:
      print('agora:',lista.pop(0))
    else:
      print('agora: pausa para café!')
    
  pessoa = input()
  
print('fila final:',lista)