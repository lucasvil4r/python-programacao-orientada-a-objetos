# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
#Lucas Vilar RA:2101658
#Gustavo Gatto RA:2201041
#Gustavo Gonçalves RA:2200601
#Kaique Fischer RA:2201268
#Juliana Vitoriano RA:2201128
#Maycon Caceres Gonçalves RA:2201047


'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e três itens e retorna 1, se os três itens estiverem armazenados
na lista, e 0 caso contrário.
'''

from array import array


def pertence(lista, item1, item2, item3):
    cont = 0
    itens = [item1, item2, item3]
    for i in range(0, len(itens)):
        if itens[i] in lista:
            cont += 1
    if cont == 3:
        return 1
    else:
        return 0

'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma tupla e dois itens (velho e novo) e retorna uma tupla onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''

def substituir(tupla, velho, novo):
    transformLista = list(tupla)
    for i in range(0, len(transformLista)):
        if transformLista[i] == velho:
            transformLista[i] = novo

    return tuple(transformLista)


'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item):
    lista = []
    for i in range(0, len(tupla)):
        if tupla[i] == item:
            lista.append(i)

    return lista
        
'''
Considere um dicionario onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada 'reprovados' que recebe como argumentos
de entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
A lista de nomes deve ser ordenada em ordem alfabética.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
'''

def reprovados(alunos):
    array = []
    for i in alunos:
        somaNota = 0
        media = 0
        for x in range(0, len(alunos[i])):
            nota = alunos[i][x]
            somaNota +=nota
        media = somaNota / len(alunos[i])
        if media < 6 :
            array.append(i)
    
    array.sort()
    return array
          

'''
Considere um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos
de entrada o dicionário, o nome de um aluno e uma nota.
A função deve excluir todas as ocorrências dessa nota do aluno informado e
retornar o dicionário com as alterações realizadas.
Se aluno não estiver no dicionário, deve retornar o dicionário sem alterações.
'''

def excluir_nota(alunos, nome, nota):
    arrayNovo = []
    for i in alunos:
        if i == nome:
            for x in range(0, len(alunos[i])):
                if alunos[i][x] != nota :
                    arrayNovo.append(alunos[i][x])

    del alunos[nome]
    alunos[nome] = arrayNovo
    return alunos


'''
Considere um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada 'menor_nota' que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a menor nota
de cada aluno.
'''

def menor_nota(alunos):
    array = []
    for i in alunos:
        for x in range(0, len(alunos[i])):
            array.append(alunos[i][x])
        menor = min(array)
        alunos[i] = menor
        array.clear()

    return alunos