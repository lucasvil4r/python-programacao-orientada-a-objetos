# Classes abstratas não podem ser instanciadas
# Métodos abstratos da classe abstrata precisam ser implementados
# obrigatoriamente em todas as suas classes filhas


from abc import ABC, abstractmethod


class Conta(ABC):                           # classe abstrata
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def consultar_saldo(self):              # método concreto
        print("Saldo: ", self.saldo)

    @abstractmethod
    def depositar(self, valor):             # método abstrato
        pass

    @abstractmethod
    def sacar(self, valor):                 # método abstrato
        pass


class ContaEspecial(Conta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.limite = limite

    def sacar(self, valor):                  # polimorfismo de inclusão
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo + Limite da conta especial é insuficiente")

    def depositar(self, valor):
        self.saldo += valor


class ContaPoupanca(Conta):
    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def calcular_juros(self):
        self.saldo = self.saldo * 1.02


print('----------------------------------------------')
conta_especial = ContaEspecial(4567, "João", 500)
conta_especial.depositar(300)
conta_especial.sacar(500)
conta_especial.consultar_saldo()

print('----------------------------------------------')
poupanca = ContaPoupanca(34567, 'Paulo')
poupanca.depositar(800)
poupanca.calcular_juros()
poupanca.consultar_saldo()
