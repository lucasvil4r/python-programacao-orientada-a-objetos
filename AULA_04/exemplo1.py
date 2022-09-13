# Realizar a divisão de dois números inteiros.
# Identificar e tratar os possíveis erros.

try:
    a = int(input('Informe um número inteiro: '))
    b = int(input('Informe um número inteiro: '))
    c = a / b
    print('Resultado da divisão: ', c)
except ZeroDivisionError:
    print("Ocorreu uma divisao por zero")
except ValueError:
    print("O numero deve ser inteiro")
except Exception:
    print("Erro inesperado")
else:               # executa quando não há erro
    print("Operacao realizada com sucesso")
finally:            # excuta sempre
    print("Fim do Programa!!!!")
