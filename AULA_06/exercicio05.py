'''
Nome da Classe:
Carro

Atributos:
quantidade_combustivel (quantidade de litros de combustível no tanque):
a quantidade inicial deve ser zero.

Métodos:
adicionar_combustivel(self, litros):
    recebe uma quantidade de litros de combustível para abastecer o tanque.
obter_combustivel(self):
    retorna a quantidade atual de combustível.
andar(self, distancia):
    recebe uma distância em km e simula o ato de dirigir o veículo
    por essa distância, reduzindo o nível de combustível no
    tanque de gasolina. Considere que o veiculo consome 0.20 litros
    de combustivel por quilômetro percorrido.
'''


class Carro:
    def __init__(self):
        self.quantidade_combustivel = 0

    def adicionar_combustivel(self, litros):
        self.quantidade_combustivel += litros

    def obter_combustivel(self):
        return self.quantidade_combustivel

    def andar(self, distancia):
        consumo = distancia * 0.20
        if self.quantidade_combustivel - consumo < 0:
            print('Não ha combustivel suficiente')
        else:
            self.quantidade_combustivel -= consumo


meu_carro = Carro()
meu_carro.adicionar_combustivel(20)     # Adiciona 20 litros
meu_carro.andar(80)                     # Andar 80 quilômetros

print('Litros de combustível no tanque:', meu_carro.obter_combustivel())
# deve imprimir: "Litros de combustível no tanque: 4.0"

meu_carro.andar(200)
print('Litros de combustível no tanque:', meu_carro.obter_combustivel())
