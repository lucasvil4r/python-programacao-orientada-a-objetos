class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        # atributos públicos
        self.nome = nome
        self.idade = idade
        # atributos privados
        self.__cpf = cpf
        self.__rg = rg

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_rg(self, rg):
        self.__rg = rg


pessoa1 = Pessoa("João", 25, "11111111111", "3333333")

print("Nome: ", pessoa1.nome)
print("Idade: ", pessoa1.idade)
print("CPF:", pessoa1.get_cpf())
print("RG:", pessoa1.get_rg())
