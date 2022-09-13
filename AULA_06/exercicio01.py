'''
Nome da classe
    Carro
Atributos:
    marca
    modelo
    placa
Métodos:
    __init__(self, marca, modelo, placa)
    exibir_dados(self)

No programa principal, crie dois objetos da classe Carro.
Utilize o método exibir_dados para exibir os atributos de cada carro.
'''


class Carro:
    # construtor
    def __init__(self, marca, modelo, placa):
        # atributo
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Placa: ', self.placa)


# cria um objeto
carro1 = Carro('Fiat', 'Siena', 'ABC-1234')
carro1.exibir_dados()

# cria outro objeto
carro2 = Carro('Ford', 'Ka', 'XYZ-4455')
carro2.exibir_dados()
