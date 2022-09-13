
def busca(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Indice inexistente"


lista = []
for i in range(5):
    nome = input("Informe um nome: ")
    lista.append(nome)

print(lista)

n = int(input('Informe um indice: '))
print(busca(lista, n))
