# ----------------------------------------------------------------
# LISTAS:

# Sequências de elementos.
# Delimitada por colchetes [ ]
lista = [3, 6, 8, 20]

# Estruturas heterogêneas: podem conter diferentes tipos de dados
lista = [2, 'abc', 4.5, 4]

# Listas vazias
lista = []

# Função print pode ser utilizada para exibir a lista no terminal
lista = [2, 5, 6]
print(lista)

# Índice: define a posição de um item na lista
# Índice inicial sempre é 0 (zero)
lista = [2, 5, 6]
print(lista[0])

# Índices negativos indicam posições referentes ao final da lista
lista = [2, 5, 6]
print(lista[-1])

# Função append: adiciona um item no final da lista
lista = [2, 5, 6]
lista.append(100)
print(lista)

# Repetição for pode ser utilizada para percorrer os itens da lista
lista = [2, 5, 6, 8, 3]
for item in lista:
    if item % 2 != 0:           # verifica se item é um número par
        print(item)

# Preencher lista com dados informados pelo usuário
lista = []
for i in range(5):
    a = int(input('Numero: '))
    lista.append(a)
print(lista)


# ----------------------------------------------------------------
# PRINCIPAIS FUNÇÕES

lista = [3, 5, 7, 8, 5, 9, 8, 10]

# len: retorna o tamanho de uma lista
print(len(lista))

# count: retorna a quantidade de ocorrências de um item na lista
print(lista.count(5))

# index: retorna o índice da primeira ocorrência de um item
# Se o item não for encontrado retorna uma exceção
print(lista.index(5))

# in: verificar se determinado item existe em uma lista
if 50 in lista:
    print('Item encontrado')
else:
    print('Item não encontrado')

# insert: insere um item em determinado índice
lista.insert(3, 200)
print(lista)

# pop: remove o último item da lista
lista.pop()
print(lista)

# pop: remove o item de um determinado índice
lista.pop(0)
print(lista)

# remove: remove a primeira ocorrência de um determinado item
lista.remove(5)
print(lista)

# sort: ordena a lista em ordem crescente
lista.sort()
print(lista)

# sort(reverse=True): ordena a lista em ordem decrescente
lista.sort(reverse=True)
print(lista)

# min: retorna o menor elemento
print(min(lista))

# max: retorna o maior elemento
print(max(lista))

# sum: retorna o somatório da lista
print(sum(lista))

# concatenação: junção de duas ou mais listas
lista1 = [4, 7, 8]
lista2 = [3, 4]
lista3 = lista1 + lista2
print(lista3)

# ----------------------------------------------------------------
