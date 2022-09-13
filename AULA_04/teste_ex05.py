from modulo_ex05 import converte_para_celsius, converte_para_fahrenheit


try:
    retorno = converte_para_celsius(32)
    assert retorno == 0
    print('CORRETO')
except AssertionError:
    print('ERRO')

try:
    retorno = converte_para_celsius(41)
    assert retorno == 5.0
    print('CORRETO')
except AssertionError:
    print('ERRO')

try:
    retorno = converte_para_fahrenheit(0)
    assert retorno == 32
    print('CORRETO')
except AssertionError:
    print('ERRO')

try:
    retorno = converte_para_fahrenheit(27)
    assert retorno == 80.6
    print('CORRETO')
except AssertionError:
    print('ERRO')
