'''
Para responder essa questão, considere uma Fila preenchida com os dígitos que compõem o seu número de RA.
Sabendo que o final da fila corresponde ao último dígito do RA, informe o estado final dessa fila após as operações abaixo:

enqueue(7)
enqueue(5)
dequeue( )
enqueue(3)
enqueue(9)
enqueue(1)
dequeue( )
enqueue(4)
dequeue( )
dequeue( )

'''

from Class.Queue import Queue #FILA - primeiro item inserido será o primeiro a ser removido

ObjQueue = Queue()

ObjQueue.enqueue(2)
ObjQueue.enqueue(1)
ObjQueue.enqueue(0)
ObjQueue.enqueue(1)
ObjQueue.enqueue(6)
ObjQueue.enqueue(5)
ObjQueue.enqueue(8)

ObjQueue.enqueue(7)
ObjQueue.enqueue(5)
ObjQueue.dequeue( )
ObjQueue.enqueue(3)
ObjQueue.enqueue(9)
ObjQueue.enqueue(1)
ObjQueue.dequeue( )
ObjQueue.enqueue(4)
ObjQueue.dequeue( )
ObjQueue.dequeue( )

print(ObjQueue)