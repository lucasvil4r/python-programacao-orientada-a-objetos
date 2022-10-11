from fila_exercicio import Fila, vira_1, vira_n

ObjStack = Fila()

ObjStack.enfileirar(1)
ObjStack.enfileirar(2)
ObjStack.enfileirar(3)
ObjStack.enfileirar(4)
ObjStack.enfileirar(5)

vira_n(ObjStack.itens, 3)

print(ObjStack.itens)