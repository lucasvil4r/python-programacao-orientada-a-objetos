from Class.Queue import Queue

ObjQueue = Queue()

ObjQueue.enqueue("Amarelo")
ObjQueue.enqueue("Branco")
ObjQueue.enqueue("Verde")
ObjQueue.enqueue("Vermelho")
ObjQueue.dequeue()
ObjQueue.dequeue()
ObjQueue.enqueue("Azul")
item = ObjQueue.dequeue()
ObjQueue.enqueue(item)

print("FILA")
print(ObjQueue.items)
