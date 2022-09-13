'''
Nome da classe
    Funcionario
Atributos:
    nome
    sobrenome
    salario_mensal
Métodos:
    __init__(self, nome, sobrenome, salario_mensal)
        O construtor deve fazer uma validação do salario_mensal,
        e se o salário mensal não for positivo, deve configurá-lo como zero.
    aumentar_salario(self)
        Aumenta o salario do funcionário em 10%
'''


class Funcionario:
    def __init__(self, nome, sobrenome, salario_mensal):
        self.nome = nome
        self.sobrenome = sobrenome
        if salario_mensal >= 0:         # verifica se o salario é positivo
            self.salario_mensal = salario_mensal
        else:
            self.salario_mensal = 0

    def aumentar_salario(self):
        self.salario_mensal += self.salario_mensal * 0.10


# cria dois objetos
func1 = Funcionario('Paulo', 'Vieira', 2000)
func2 = Funcionario('Maria', 'Silva', -4000)

# aumenta salário dos funcionarios
func1.aumentar_salario()
func2.aumentar_salario()

# exibe salário dos funcionarios
print('Salario: ', func1.salario_mensal)    # Salario:  2200.0
print('Salario: ', func2.salario_mensal)    # Salario:  0.0
