class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_resultado(self):
        print("Nome do Medico: ", self.medico.nome)
        print("CRM do medico: ", self.medico.crm)
        print("Especialidade: ", self.medico.especializacao)
        print("Nome do paciente: ", self.paciente.nome)
        print("CPF do paciente: ", self.paciente.cpf)
        print("Idade do paciente: ", self.paciente.idade)
        print("Descrição do exame: ", self.descricao)
        print("Resultado: ", self.resultado)


paciente1 = Paciente("Paulo", '3333333333', 26)
medico1 = Medico("Ana", "34344", "Clinico Geral")
exame1 = Exame(medico1, paciente1, "COVID-19", "Negativo")

exame1.imprimir_resultado()
