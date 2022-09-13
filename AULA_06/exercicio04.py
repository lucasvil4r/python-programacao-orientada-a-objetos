'''
Nome da classe
    Aluno
Atributos:
    ra
    nome
    turma
    notas (lista que deve ser inicializada como vazia)
Métodos:
    __init__(self, ra, nome, turma)
    inserir_nota(self, nota)
    calcular_media(self)

Crie 3 objetos da classe aluno. Insira algumas notas para os alunos.
Insira os objetos em uma lista.
Percorra a lista, calcule e exiba a média aritmética de cada aluno.
'''


class Aluno:
    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        media = sum(self.notas) / 2
        return media


# cria os Alunos
aluno1 = Aluno(123456, 'Paulo', '2A')
aluno2 = Aluno(456789, 'João', '2A')
aluno3 = Aluno(678765, 'Ana', '2A')

# insere as notas dos alunos
aluno1.inserir_nota(8)
aluno1.inserir_nota(7)

aluno2.inserir_nota(10)
aluno2.inserir_nota(6)

aluno3.inserir_nota(7.5)

# lista de objetos da classe Aluno
lista = [aluno1, aluno2, aluno3]

# percorre alista de alunos
for x in lista:
    print(x.nome, x.calcular_media())
