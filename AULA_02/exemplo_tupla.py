# ----------------------------------------------------------------
# TUPLAS

# Sequências de elementos que não podem ser alteradas
# Delimitada por parenteses ( )
tupla = (4, 7, 8)

# Estruturas heterogêneas: podem conter diferentes tipos de dados
tupla = (2, 'abc', 4.5, 4)

# tuplas vazias
tupla = ()

# tuplas de 1 elemento (tem uma vírgula no final)
tupla = (10,)
print(tupla)

# Índice: define a posição de um item na tupla
# Índice inicial sempre é 0 (zero)
tupla = (4, 6, 7, 8)
print(tupla[1])

# Índices negativos indicam posições referentes ao final da tupla
tupla = (2, 5, 6)
print(tupla[-1])

# Repetição for pode ser utilizada para percorrer os itens da tupla
for item in tupla:
    print(item)


# ----------------------------------------------------------------
# PRINCIPAIS FUNÇÕES

tupla = (3, 5, 7, 8, 5, 9, 8, 10)

# len: retorna o tamanho de uma tupla
print(len(tupla))

# count: retorna a quantidade de ocorrências de um item na tupla
print(tupla.count(5))

# index: retorna o índice da primeira ocorrência de um item
# Se o item não for encontrado retorna uma exceção
print(tupla.index(5))

# min: retorna o menor elemento
print(min(tupla))

# max: retorna o maior elemento
print(max(tupla))

# sum: retorna o somatório da tupla
print(sum(tupla))

# in: verificar se determinado item existe em uma tupla
if 50 in tupla:
    print('Item encontrado')
else:
    print('Item não encontrado')

# concatenção de tuplas
tupla1 = (3, 5, 6)
tupla2 = (5, 7, 8)
tupla3 = tupla1 + tupla2
print(tupla3)

# ----------------------------------------------------------------
