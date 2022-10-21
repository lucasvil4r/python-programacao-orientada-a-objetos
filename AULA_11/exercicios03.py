from Class.Stack import Stack

ObjStack = Stack()

ObjStack.push(7)
ObjStack.push(5)
ObjStack.pop()
ObjStack.push(3)
ObjStack.push(9)
ObjStack.push(1)
ObjStack.pop()
ObjStack.push(4)
ObjStack.pop()
ObjStack.pop()

print(ObjStack.stack)
