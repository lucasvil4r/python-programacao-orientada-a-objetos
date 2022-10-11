from Class.Stack import Stack

ObjStack = Stack()

ObjStack.push(10)
ObjStack.push(5)
ObjStack.push(3)
ObjStack.push(50)
ObjStack.pop()
ObjStack.push(11)
ObjStack.push(9)
ObjStack.push(20)
ObjStack.pop()
ObjStack.pop()

print(ObjStack.items)
