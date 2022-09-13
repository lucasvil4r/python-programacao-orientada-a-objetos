lista = []
for a in range(10):
    n = int(input("Informe um numero inteiro: "))
    lista.append(n)

print(lista)

contador = 0
somador = 0
for item in lista:
    if item % 2 == 0:
        contador += 1
    else:
        somador += item

print('Quantidade de pares:', contador)
print('somatório de ímpares:', somador)
