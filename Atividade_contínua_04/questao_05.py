'''
Para responder essa questão, considere uma Pilha preenchida com os dígitos que compõem o seu número de RA.
Sabendo que o topo da pilha corresponde ao último dígito do RA, informe o estado final dessa pilha após as operações abaixo:

desempilhar( )
desempilhar( )
desempilhar( )
empilhar(5)
empilhar(7)
empilhar(3)
desempilhar( )
desempilhar( )

'''

from Class.Stack import Stack #PILHA - primeiros serão os últimos a serem removidos

ObjStack = Stack()

RA = 2101658

ObjStack.push(2)
ObjStack.push(1)
ObjStack.push(0)
ObjStack.push(1)
ObjStack.push(6)
ObjStack.push(5)
ObjStack.push(8)

ObjStack.pop()
ObjStack.pop()
ObjStack.pop()
ObjStack.push(5)
ObjStack.push(7)
ObjStack.push(3)
ObjStack.pop()
ObjStack.pop()

print(ObjStack)
