# ARQUIVO DE TESTE PARA A ATIVIDADE CONTÍNUA 02
# Este arquivo não deve ser modificado.

# Importa as classes do módulo ac02
from ac02 import Endereco, Cliente, Pedido, Historico


# Criação do Endereço
try:
    endereco = Endereco("Avenida Brasil", "123", "Apto. 58", "Centro",
                        "São Paulo", "SP", "05577-023")
    assert endereco.rua == 'Avenida Brasil'
    assert endereco.numero == '123'
    assert endereco.complemento == 'Apto. 58'
    assert endereco.bairro == 'Centro'
    assert endereco.cidade == 'São Paulo'
    assert endereco.uf == 'SP'
    assert endereco.cep == '05577-023'
except AssertionError:
    print('ERRO...: valor dos atributos do Endereco')
except Exception:
    print('ERRO...: criação do Endereco')
else:
    print('CORRETO: criação do Endereco')


# Criação do Cliente
try:
    cliente = Cliente("Paulo", "(11) 99999-4565", endereco)
    assert cliente.nome == 'Paulo'
    assert cliente.telefone == '(11) 99999-4565'
    assert cliente.endereco.rua == 'Avenida Brasil'
except AssertionError:
    print('ERRO...: valor dos atributos do Cliente')
except Exception:
    print('ERRO...: criação do Cliente')
else:
    print('CORRETO: criação do Cliente')


# Criação do Primeiro Pedido
try:
    pedido1 = Pedido(cliente, 1.0, 3.0, "10 vezes sem juros",
                     "cinza", "vermelha")
    assert pedido1.cliente.nome == 'Paulo'
    assert pedido1.altura == 1.0
    assert pedido1.largura == 3.0
    assert pedido1.frase == '10 vezes sem juros'
    assert pedido1.cor_placa == 'cinza'
    assert pedido1.cor_letra == 'vermelha'
except AssertionError:
    print('ERRO...: valor dos atributos do primeiro Pedido')
except Exception:
    print('ERRO...: criação do primeiro Pedido')
else:
    print('CORRETO: criação do primeiro Pedido')


# Criação do Segundo Pedido
try:
    pedido2 = Pedido(cliente, 0.5, 2, "Estamos Atendendo", "cinza", "vermelha")
    assert pedido2.cliente.nome == 'Paulo'
    assert pedido2.altura == 0.5
    assert pedido2.largura == 2
    assert pedido2.frase == 'Estamos Atendendo'
    assert pedido2.cor_placa == 'cinza'
    assert pedido2.cor_letra == 'vermelha'
except AssertionError:
    print('ERRO...: valor dos atributos do segundo Pedido')
except Exception:
    print('ERRO...: criação do segundo Pedido')
else:
    print('CORRETO: criação do segundo Pedido')


# Criação do Terceiro Pedido
try:
    pedido3 = Pedido(cliente, 2, 5, "Promoção de inauguração",
                     "branca", "preta")
    assert pedido3.cliente.nome == 'Paulo'
    assert pedido3.altura == 2
    assert pedido3.largura == 5
    assert pedido3.frase == 'Promoção de inauguração'
    assert pedido3.cor_placa == 'branca'
    assert pedido3.cor_letra == 'preta'
except AssertionError:
    print('ERRO...: valor dos atributos do terceiro Pedido')
except Exception:
    print('ERRO...: criação do terceiro Pedido')
else:
    print('CORRETO: criação do terceiro Pedido')


# Inserção dos pedidos no histórico
try:
    historico = Historico()
    historico.inserir_pedido(pedido1)
    historico.inserir_pedido(pedido2)
    historico.inserir_pedido(pedido3)
except Exception:
    print('ERRO...: inserção dos pedidos no Historico')
else:
    print('CORRETO: inserção dos pedidos no Historico')


# Valor total do primeiro pedido
try:
    assert pedido1.calcular_total() == 446.25
except AssertionError:
    print('ERRO...: valor total do primeiro pedido')
except Exception:
    print('ERRO...: valor total do primeiro pedido')
else:
    print('CORRETO: valor total do primeiro pedido')


# Valor total do segundo pedido
try:
    assert pedido2.calcular_total() == 152.6
except AssertionError:
    print('ERRO...: valor total do segundo pedido')
except Exception:
    print('ERRO...: valor total do segundo pedido')
else:
    print('CORRETO: valor total do segundo pedido')


# Valor total do terceiro pedido
try:
    assert pedido3.calcular_total() == 1477.35
except AssertionError:
    print('ERRO...: valor total do terceiro pedido')
except Exception:
    print('ERRO...: valor total do terceiro pedido')
else:
    print('CORRETO: valor total do terceiro pedido')


# Faturamento total
try:
    assert historico.calcular_faturamento() == 2076.2
except AssertionError:
    print('ERRO...: calcular faturamento')
except Exception:
    print('ERRO...: calcular faturamento')
else:
    print('CORRETO: calcular faturamento')
