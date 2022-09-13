# importação relativa
from math import sqrt, factorial
from random import randint as sorteio  # renomeiar módulo

from modulo1 import soma, exibe_numeros

numero = sqrt(20)
print(numero)

resultado = factorial(5)
print(resultado)

n = sorteio(1, 50)
print(n)

c = soma(3, 7)
print(c)

exibe_numeros()
