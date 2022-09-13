
produtos = {}

for i in range(5):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    produtos[nome] = preco

print(produtos)             # exibe o dicionário

for nome in produtos:       # percorre o dicionario
    if produtos[nome] > 50:
        print(nome, produtos[nome])
