'''
Escreva uma função chamada intercala_numeros que recebe como
entrada duas listas de três elementos e retorna uma lista de seis elementos,
com os números intercalados.

Exemplo: Suponha que as listas de entrada da função sejam:
[1, 2, 3]
[4, 5, 6]
Para estas listas, a função deve retornar:
[1, 4, 2, 5, 3, 6]
'''


def intercala_numeros(lista1, lista2):
    lista3 = []
    for i in range(3):          # i=[0, 1, 2]
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = intercala_numeros(lista1, lista2)
print(lista3)
