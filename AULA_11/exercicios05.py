'''
Considere que os números 10, 11, 12, 13, 14 foram inseridos,
nessa ordem, em uma fila. Posteriormente esses mesmos números
foram inseridos também, na mesma ordem, em uma pilha. Nesse caso:

o último elemento a ser removido da fila é o número 14.
o primeiro elemento a ser removido da pilha é o número 10.
o topo da pilha é o número 10.
o número 14 é o primeiro elemento a ser removido da fila.

'''

from Class.Queue import Queue

ObjStack = Queue()

ObjStack.enqueue(10)
ObjStack.enqueue(11)
ObjStack.enqueue(12)
ObjStack.enqueue(13)
ObjStack.enqueue(14)
ObjStack.dequeue()

print("FILA")
print(ObjStack.items)
  
print("-"*10)
from Class.Stack import Stack

ObjStack = Stack()

ObjStack.push(10)
ObjStack.push(11)
ObjStack.push(12)
ObjStack.push(13)
ObjStack.push(14)
ObjStack.pop()

print("PILHA")
print(ObjStack.items)
