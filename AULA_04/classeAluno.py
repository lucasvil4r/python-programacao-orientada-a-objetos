'''
Criar uma classe Aluno
- Atributos: ra, nome, email, lista de notas.
- Métodos: inserir_nota, calcular_media
'''
class Aluno:
    def __init__(self, ra, nome, email):        # construtor
        # atributos
        self.ra = ra
        self.nome = nome
        self.email = email
        self.lista_notas = []       # inicializa com uma lista vazia

    # Métodos
    def inserir_nota(self, nota):
        self.lista_notas.append(nota)

    def calcular_media(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
        return media


# cria objeto
aluno1 = Aluno(1111111, 'Paulo', 'paulo@email.com')
# insere notas
aluno1.inserir_nota(9.5)
aluno1.inserir_nota(7)
aluno1.inserir_nota(8.5)
# calcula a media
print('Média: ', aluno1.calcular_media())
