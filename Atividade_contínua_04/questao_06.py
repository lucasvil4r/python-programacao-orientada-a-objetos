'''
Para responder essa questão, considere uma Fila preenchida com os dígitos que compõem o seu número de RA. 
Sabendo que o final da fila corresponde ao último dígito do RA, informe o estado final dessa fila após as operações abaixo:

enfileirar(5)
enfileirar(1)
desenfileirar( )
enfileirar(5)
desenfileirar( )
enfileirar(7)
enfileirar(3)
enfileirar(2)
desenfileirar( )

'''

from Class.Queue import Queue #FILA - primeiro item inserido será o primeiro a ser removido

ObjQueue = Queue()

RA = 2101658

ObjQueue.enqueue(2)
ObjQueue.enqueue(1)
ObjQueue.enqueue(0)
ObjQueue.enqueue(1)
ObjQueue.enqueue(6)
ObjQueue.enqueue(5)
ObjQueue.enqueue(8)

ObjQueue.enqueue(5)
ObjQueue.enqueue(1)
ObjQueue.dequeue()
ObjQueue.enqueue(5)
ObjQueue.dequeue()
ObjQueue.enqueue(7)
ObjQueue.enqueue(3)
ObjQueue.enqueue(2)
ObjQueue.dequeue()

print(ObjQueue)