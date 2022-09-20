class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


lista_filmes = []

for i in range(3):
    titulo = input("Titulo do filme: ")
    genero = input("Genero do filme: ")
    filme = Filme(titulo, genero)
    lista_filmes.append(filme)

for filme in lista_filmes:
    print("Titulo:", filme.get_titulo(), "Genero:", filme.get_genero())
