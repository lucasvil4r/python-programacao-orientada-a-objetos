'''
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| descricao  |0..*    1| cliente             |1      1| nome        |
| valor      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produtos()   |
                       | calcular_total()    |
                       |---------------------|
'''


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print("Descrição: ", produto.descricao, "Valor: ", produto.valor)

    def calcular_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma

cliente1 = Cliente("João da Silva")

produto1 = Produto("Teclado", 80)
produto2 = Produto("Pen Drive", 30)

carrinho1 = Carrinho(cliente1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto2)

carrinho1.listar_produtos()
print("Total: ", carrinho1.calcular_total())
