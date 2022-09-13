'''
Criar uma classe Pessoa.
- Atributos: nome, email, telefone.
- Métodos: Um método deve exibir os dados desta pessoa.
'''


class Pessoa:
    def __init__(self, nome, email, telefone):             # construtor
        # atributos
        self.nome = nome
        self.email = email
        self.telefone = telefone

    # metodos
    def exibir(self):
        print('-'*30)
        print('Nome: ', self.nome)
        print('Email: ', self.email)
        print('Telefone: ', self.telefone)


# cria um objeto
pessoa1 = Pessoa('paulo', 'paulo@email.com', 119999999)
pessoa1.exibir()

# cria outro objeto
pessoa2 = Pessoa('Maria', 'maria@email.com', 11984847584)
pessoa2.exibir()

# exemplo de cadastro pelo usuário
nome = input('Informe o Nome: ')
telefone = int(input('Informe o Telefone: '))
email = input('Informe o Email: ')
# cria objeto com as informações digitadas
pessoa3 = Pessoa(nome, email, telefone)
pessoa3.exibir()