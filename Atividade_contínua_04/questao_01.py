'''
Ao inserirmos em uma estrutura de dados do tipo Pilha os seguintes elementos: A, B, C e D, exatamente nesta ordem. 
E em seguida realizarmos duas operações consecutivas de remoção na pilha e imediatamente inserirmos dois novos elementos: X e W. 
Podemos afirmar que ao realizarmos uma nova operação de remoção, o elemento que será removido desta pilha será o:
'''

from Class.Stack import Stack

ObjStack = Stack()

A = 1
B = 2
C = 3
D = 4
X = 5
W = 6

ObjStack.push(A)
ObjStack.push(B)
ObjStack.push(C)
ObjStack.push(D)
ObjStack.pop()
ObjStack.pop()
ObjStack.push(X)
ObjStack.push(W)
ObjStack.pop()

print(ObjStack.stack)

#output [1, 2, 5] = W removido