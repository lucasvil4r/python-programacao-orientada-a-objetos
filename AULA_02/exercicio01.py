lista = []
for a in range(10):
    n = int(input("Informe um numero inteiro: "))
    lista.append(n)

print(lista)

maior = max(lista)
print('Maior:', maior)

menor = min(lista)
print('Menor:', menor)

media = sum(lista) / len(lista)
print('Média:', media)
