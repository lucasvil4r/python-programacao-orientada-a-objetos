# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Nathalia de Araujo Santos - 2201044
# ALUNO 2: Lucas Vilar - 2101658
# ALUNO 3: GUSTAVO GATTO - 2201041
# ALUNO 4:
# ALUNO 5:
# ALUNO 6:

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


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = 147.00
        self.__valor_fixo_letra = 0.35
        self.valor_final = 0
    
    def calcular_total(self):
        area = self.altura * self.largura
        custo_material = area * self.__valor_fixo_material
        
        self.frase = self.frase.replace(" ", "")
        numero_letras = len(self.frase)

        custo_desenho = numero_letras * self.__valor_fixo_letra
        valor_placa = custo_material + custo_desenho
        self.valor_final = valor_placa

        return valor_placa


class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def calcular_faturamento(self):
        listSum = 0
        for number in range(len(self.__pedidos)):
            listSum += self.__pedidos[number].valor_final

        return listSum
