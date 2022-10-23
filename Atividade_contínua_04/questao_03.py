'''
Sobre listas, filas e pilhas, considere as afirmativas a seguir e assinale a alternativa correta.
I. As estruturas de dados pilhas e filas armazenam coleções de itens. A diferença entre elas é a ordem em que podem ser retirados os itens dessas coleções.
II. Considere que os itens A, B, C, D e E foram inseridos nessa ordem em uma fila. Necessariamente, o primeiro item a ser removido dessa fila é o item A.
III. Considere que os itens A, B, C, D e E foram inseridos nessa ordem em uma pilha. Necessariamente, o último item a ser removido dessa pilha é o item E.
IV. Considere que os itens A, B, C, D e E foram inseridos nessa ordem em uma lista. Necessariamente, o primeiro item a ser removido dessa lista é o item A.
'''


from Class.Queue import Queue #IMPORTANDO CLASSE FILA

ObjQueue = Queue()

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'

ObjQueue.enqueue(A)
ObjQueue.enqueue(B)
ObjQueue.enqueue(C)
ObjQueue.enqueue(D)
ObjQueue.enqueue(E)
ObjQueue.dequeue()

print(ObjQueue)
