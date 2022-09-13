lista1 = []
lista2 = []

for i in range(5):
    n = int(input('Numero: '))
    lista1.append(n)
print(lista1)

for i in range(5):
    n = int(input('Numero: '))
    lista2.append(n)
print(lista2)

tupla1 = tuple(lista1)      # tuple: converte lista para tupla
tupla2 = tuple(lista2)

tupla3 = tupla1 + tupla2
print(tupla3)
