'''
Classe Cachorro
- Atributos: nome, idade
- Métodos: andar, comer, latir
'''
class Cachorro:
    # construtor (utilizado para definir os atributos da classe)
    def __init__(self, nome, idade):
        # atributos
        self.nome = nome
        self.idade = idade

    # metodos
    def andar(self, distancia):
        print("O cachorro andou", distancia, "metros")

    def comer(self):
        print("O cachorro de nome", self.nome, "comeu")

    def latir(self):
        print("O cachorro latiu")


# cria uma instancia (objeto) da classe Cachorro
dog = Cachorro("Rex", 4)
print("O cachorro", dog.nome, "possui", dog.idade, "anos")
dog.andar(10)
dog.comer()
dog.latir()

# cria outra instancia (objeto) da classe Cachorro
meu_cachorro = Cachorro("Snoopy", 2)
print("O cachorro", dog.nome, "possui", dog.idade, "anos")
meu_cachorro.andar(5)
meu_cachorro.latir()
# altera a idade do cachorro
meu_cachorro.idade = 3
print("O cachorro", dog.nome, "possui", dog.idade, "anos")