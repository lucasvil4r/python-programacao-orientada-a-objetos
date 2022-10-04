class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cachorro(Animal):
    def emitir_som(self):
        print('AUAU')


class Gato(Animal):
    def emitir_som(self):
        print('Miaw')


class Cavalo(Animal):
    def emitir_som(self):
        print('Cavalo Emitindo Som')


class Veterinario:
    def examinar(self, animal):
        animal.emitir_som()


dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()
horse.emitir_som()
cat.emitir_som()

vet = Veterinario()
vet.examinar(dog)
vet.examinar(horse)
vet.examinar(cat)







