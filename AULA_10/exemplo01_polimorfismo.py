class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def consultar_saldo(self):
        print("Saldo: ", self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo da conta é insuficiente")


class ContaEspecial(Conta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.limite = limite

    def sacar(self, valor):     # sobrescreve o método herdado da superclasse
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print('Saldo e limite insuficientes')


print('----------------------------------------------')
conta = Conta(1234, 'Paulo')
conta.depositar(300)
conta.sacar(500)
conta.consultar_saldo()

print('----------------------------------------------')
conta_especial = ContaEspecial(4567, "João", 500)
conta_especial.depositar(300)
conta_especial.sacar(500)
conta_especial.consultar_saldo()
