from abc import abstractmethod


class Operacao:
    @abstractmethod
    def Calcular(self, x, y):
        pass

class Soma(Operacao):
    def Calcular(self, x, y):
        return x + y

class Subtracao(Operacao):
    def Calcular(self, x, y):
        return x - y

class Multiplicacao(Operacao):
    def Calcular(self, x, y):
        return x * y

class Divisao(Operacao):
    def Calcular(self, x, y):
        return x / y


soma = Soma()
sub = Subtracao()
mult = Multiplicacao()
div = Divisao()

print(soma.Calcular(10,5))
print(sub.Calcular(10,5))
print(mult.Calcular(10,5))
print(div.Calcular(10,5))
