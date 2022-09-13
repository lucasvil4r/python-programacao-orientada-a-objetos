# Arquivo de Teste

from modulo import soma, media_lista

try:
    resultado = soma(10, 5)
    assert resultado == 15
    print('CORRETA')
except AssertionError:
    print('ERRADA')

try:
    resultado = soma(-20, -30)
    assert resultado == -50
    print('CORRETA')
except AssertionError:
    print('ERRADA')

try:
    resultado = media_lista([3, 4, 5, 6, 7])
    assert resultado == 5
    print('CORRETA')
except AssertionError:
    print('ERRADA')
