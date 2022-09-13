class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        percentual = self.salario * percentual / 100
        return self.salario + percentual

nome = input('')
salario = int(input())

obj1 = Funcionario(nome, salario)
print(obj1.aumentar_salario(10))
