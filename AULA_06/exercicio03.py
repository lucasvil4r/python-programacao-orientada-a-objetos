class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor, senha):
        if senha == self.senha:         # validar a senha
            self.saldo += valor
        else:
            print('Senha Inválida')

    def sacar(self, valor, senha):
        if senha == self.senha:         # validar a senha
            if valor <= self.saldo:     # verificar se tem saldo suficiente
                self.saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('Senha Inválida')


conta1 = ContaBancaria(678, 'Paulo Vieira', 123456)

valor = float(input('Valor para deposito: '))
senha = int(input('Digite a senha: '))
conta1.depositar(valor, senha)
print(conta1.saldo)

valor = float(input('Valor para saque: '))
senha = int(input('Digite a senha: '))
conta1.sacar(valor, senha)
print(conta1.saldo)
