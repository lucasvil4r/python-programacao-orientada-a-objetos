from fila_exercicio import Fila, vira_1, vira_n

try:
    fila = Fila()
    assert fila.itens == []
    fila.enfileirar(1)
    assert fila.itens == [1]
    fila.enfileirar(2)
    assert fila.itens == [1, 2]
    fila.enfileirar(5)
    assert fila.itens == [1, 2, 5]
    fila.enfileirar(10)
    assert fila.itens == [1, 2, 5, 10]
    assert fila.tamanho() == 4

    valor = fila.desenfileirar()
    assert valor == 1
    assert fila.itens == [2, 5, 10]
    assert fila.tamanho() == 3
    valor = fila.desenfileirar()
    assert valor == 2
    assert fila.itens == [5, 10]
    assert fila.vazia() is False
    valor = fila.desenfileirar()
    assert valor == 5
    assert fila.itens == [10]
    assert fila.tamanho() == 1
    valor = fila.desenfileirar()
    assert valor == 10
    assert fila.itens == []
    assert fila.vazia() is True
    assert fila.tamanho() == 0

    fila.enfileirar(4)
    fila.enfileirar(20)
    fila.enfileirar(10)
    valor = fila.primeiro()
    assert valor == 4
    assert fila.itens == [4, 20, 10]
    valor = fila.desenfileirar()
    valor = fila.primeiro()
    assert valor == 20
    assert fila.itens == [20, 10]
    print("FILA CORRETA")
except AssertionError:
    print("FILA COM ERRO")


try:
    fila = Fila()
    fila.enfileirar(1)
    fila.enfileirar(2)
    fila.enfileirar(3)
    fila.enfileirar(10)
    vira_1(fila)
    assert fila.itens == [2, 3, 10, 1]
    vira_1(fila)
    assert fila.itens == [3, 10, 1, 2]
    print("vira_1 CORRETA")
except AssertionError:
    print("vira_1 COM ERRO")


try:
    fila = Fila()
    fila.enfileirar(1)
    fila.enfileirar(2)
    fila.enfileirar(3)
    fila.enfileirar(10)
    vira_n(fila, 3)
    assert fila.itens == [10, 1, 2, 3]
    vira_n(fila, 5)
    assert fila.itens == [1, 2, 3, 10]
    print("vira_n CORRETA")
except AssertionError:
    print("vira_n COM ERRO")
