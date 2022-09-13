from calendar import c


class Livro:
    def __init__(self, titulo, autor, qtdPage):        # construtor
        # atributos
        self.titulo = titulo
        self.autor = autor
        self.qtdPage = qtdPage

livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 264)
livro2 = Livro("Poeira em alto mar", "Alan Bida", 100)

print(livro1.titulo, livro1.autor, livro1.qtdPage)
print(livro2.titulo, livro2.autor, livro2.qtdPage)