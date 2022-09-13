lista = []
for i in range(10):
    n = int(input('Número: '))
    lista.append(n)

print(lista)

pares = []
impares = []

for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print(pares)
print(impares)
