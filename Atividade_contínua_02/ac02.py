# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1:
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:
# ALUNO 6:


from multiprocessing.heap import Arena


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

class Historico:
    def __init__(self, pedidos):
        self.__pedidos = pedidos

    #def inserir_pedido(self):

class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra, valor_fixo_material, valor_fixo_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = valor_fixo_material
        self.__valor_fixo_letra = valor_fixo_letra

    def calcular_total(self):
        area = self.altura * self.largura
        custo_material = area * 147.00
        custo_desenho = self.__valor_fixo_letra * 0.35
        valor_placa = custo_material + custo_desenho

        return valor_placa
        '''
        área = altura x largura
        custo_material = área x R$ 147,00
        custo_desenho = número_letras x R$ 0,35 (espaços devem ser desconsiderados)
        valor_placa = custo_material + custo_desenho
        '''



# Criação do Endereço
endereco = Endereco("Avenida Brasil", "123", "Apto. 58", "Centro", "São Paulo", "SP", "05577-023")
endereco.rua == 'Avenida Brasil'
endereco.numero == '123'
endereco.complemento == 'Apto. 58'
endereco.bairro == 'Centro'
endereco.cidade == 'São Paulo'
endereco.uf == 'SP'
endereco.cep == '05577-023'


'''
# Criação do Cliente
cliente = Cliente("Paulo", "(11) 99999-4565", endereco)
cliente.nome == 'Paulo'
cliente.telefone == '(11) 99999-4565'
cliente.endereco.rua == 'Avenida Brasil'

# Criação do Primeiro Pedido
pedido1 = Pedido(cliente, 1.0, 3.0, "10 vezes sem juros", "cinza", "vermelha")
pedido1.cliente.nome == 'Paulo'
pedido1.altura == 1.0
pedido1.largura == 3.0
pedido1.frase == '10 vezes sem juros'
pedido1.cor_placa == 'cinza'
pedido1.cor_letra == 'vermelha'

# Criação do Segundo Pedido
pedido2 = Pedido(cliente, 0.5, 2, "Estamos Atendendo", "cinza", "vermelha")
pedido2.cliente.nome == 'Paulo'
pedido2.altura == 0.5
pedido2.largura == 2
pedido2.frase == 'Estamos Atendendo'
pedido2.cor_placa == 'cinza'
pedido2.cor_letra == 'vermelha'

# Criação do Terceiro Pedido
pedido3 = Pedido(cliente, 2, 5, "Promoção de inauguração","branca", "preta")
pedido3.cliente.nome == 'Paulo'
pedido3.altura == 2
pedido3.largura == 5
pedido3.frase == 'Promoção de inauguração'
pedido3.cor_placa == 'branca'
pedido3.cor_letra == 'preta'

# Inserção dos pedidos no histórico
historico = Historico()
historico.inserir_pedido(pedido1)
historico.inserir_pedido(pedido2)
historico.inserir_pedido(pedido3)

# Valor total do primeiro pedido
pedido1.calcular_total() == 446.25

# Valor total do segundo pedido
pedido2.calcular_total() == 152.6

# Valor total do terceiro pedido
pedido3.calcular_total() == 1477.35

# Faturamento total
historico.calcular_faturamento() == 2076.2
'''

