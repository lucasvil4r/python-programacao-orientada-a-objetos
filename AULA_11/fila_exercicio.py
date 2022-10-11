'''
FILA:

Uma fila é uma estrutura de dados que suporta 2 operações
basicas: enfileirar e desenfileirar.

A idéia é que novos itens são enfileirados "no fim" da fila,
e os itens removidos são desenfileirados do final da fila.

Ou seja: quem entrou primeiro, sai primeiro.
Em inglês: First In First Out (FIFO).

EXERCÍCIO 1:
Implemente os métodos da classe Fila, definidos abaixo.

EXERCICIO 2:
    Implemente a funcao vira_1(fila) que recebe uma fila, retira o primeiro
    item do começo da fila e coloca ele de volta, no fim da fila.

    Exemplo: se uma fila contém os itens [1, 2, 3, 4, 5] e fizermos
    vira_1(fila), a fila passa a ser [2, 3, 4, 5, 1]

    DICA: Utilize os métodos enfileirar e desenfileirar.

EXERCICIO 3:
    Implemente a funcao vira_n(fila, n) que recebe uma fila, retira N
    itens do começo da fila e coloca eles de volta, no fim da fila.

    Exemplo: se uma fila contém os itens [1, 2, 3, 4, 5] e fizermos
    vira_n(fila, 3), a fila passa a ser [4, 5, 1, 2, 3]

    DICA: Utilize os métodos enfileirar e desenfileirar.
'''

class Fila:
    def __init__(self):
        '''Inicializa uma fila vazia'''
        self.itens = []

    def enfileirar(self, item):
        '''Insere um item no final da fila'''
        """Enqueue (enfileirar) é o mesmo que append"""
        self.itens.append(item)

    def desenfileirar(self):
        '''Remove o item do início da fila e retorna esse item.'''
        retorna = self.itens[0]
        del self.itens[0]
        return retorna

    def tamanho(self):
        '''Retorna a quantidade de itens na fila.'''
        return len(self.itens)

    def vazia(self):
        '''Retorna True se a fila estiver vazia, e False caso contrário'''
        if (len(self.itens) == 0):
            return True
        else:
            return False

    def primeiro(self):
        '''Retorna o primeiro item da fila sem remove-lo da fila'''
        return self.itens[0]

def vira_1(lista):
    varTemp = lista[0]
    del lista[0]
    lista.append(varTemp)

def vira_n(lista, qtdIndice):
    for i in range(qtdIndice):
        varTemp = lista[qtdIndice]
        del lista[qtdIndice]
        lista.append(varTemp)
