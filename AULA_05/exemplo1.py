class Cachorro:
    # Construtor da classe
    def __init__(self, nome, idade, raca):
        # atributos da classe
        self.nome = nome
        self.idade = idade
        self.raca = raca

    # Métodos da classe
    def latir(self):
        print('Cachorro', self.nome ,'latindo')

    def dormir(self):
        print('Cachorro dormindo')


# Criação de objetos
cachorro1 = Cachorro('Rex', 4, 'Dalmata')
cachorro2 = Cachorro('Snoopy', 3, 'Buldogue')

# Alteração de atributo do objeto
cachorro1.idade = 5

# Execução de método da classe
cachorro1.latir()
cachorro2.latir()
