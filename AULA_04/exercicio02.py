def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 99]
    for i in range(15):
        try:
            print(lista[i])
        except IndexError:
            print("Foi acessado um indice inexistente: ", i)
    # continua executando
    print('Fim da função')


print('Início do programa')
funcao_1()
print('Fim do programa')
