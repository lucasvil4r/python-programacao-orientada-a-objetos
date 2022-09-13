class Pessoa:
    def __init__(self, nome, idade, carro):
        self.nome = nome
        self.idade = idade
        self.carro = carro


class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25, meucarro)

print('Nome: ', eu.nome)                                # João
print('Idade: ', eu.idade)                              # 25
print('Marca do carro: ', eu.carro.marca)               # Volkswagen
print('Modelo do carro: ', eu.carro.modelo)             # Gol
print('Placa do carro: ', eu.carro.placa)               # AAA-1111
print('Ano do carro: ', eu.carro.ano)                   # 2015
