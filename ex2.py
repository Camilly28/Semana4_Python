notas = input()
lista_notas = []
for x in notas.split():
    lista_notas.append(float(x))
lista_notas.sort()
lista_notas.reverse()
print(lista_notas)
