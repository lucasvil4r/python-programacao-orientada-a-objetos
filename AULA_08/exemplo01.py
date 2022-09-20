'''

Exemplo de Associação de Classes:

|-------------------|           |-------------------|
| Pessoa            |           | Endereco          |
|-------------------|           |-------------------|
| nome              |           | rua               |
| idade             |-----------| numero            |
| endereco          |           | complemento       |
|-------------------|           | cep               |
| exibir_dados()    |           |-------------------|
|-------------------|           | exibir_dados()    |
                                |-------------------|
'''


class Endereco:
    def __init__(self, rua, numero, complemento, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep

    def exibir_dados(self):
        print("Rua: ", self.rua)
        print("Numero: ", self.numero)
        print("Complemento: ", self.complemento)
        print("CEP: ", self.cep)


class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        self.endereco.exibir_dados() # executa método do endereço


# Cria objeto Endereco
end1 = Endereco("Av. Paulista", 100, 'apto 20', 999999999)

# Cria objeto Pessoa e associa o objeto Endereco a ela
pessoa1 = Pessoa("Paulo", 25, end1)

pessoa1.exibir_dados()
