#FILA - primeiro item inserido será o primeiro a ser removido
from typing import Deque, Any
from collections import deque

class Queue:
    """Uma classe representando uma fila"""

    def __init__(self, maxlen=None) -> None:
        # Deque permite enviar maxlen
        # para criar um tamanho máximo para
        # a fila
        self.items: Deque[Any] = deque(maxlen=maxlen)

    def enqueue(self, *items: Any) -> None:
        """Enqueue (enfileirar) é o mesmo que append"""
        for item in items:
            self.items.append(item)

    def dequeue(self) -> Any:
        """Dequeue (desenfileirar) é o mesmo que popleft"""
        if not self:
            raise IndexError('pop from empty queue')
        return self.items.popleft()

    def __repr__(self) -> str:
        return str(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def __len__(self) -> int:
        return len(self.items)
