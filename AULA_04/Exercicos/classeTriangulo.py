class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        # atributos
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        soma = self.lado_a + self.lado_b + self.lado_c
        return soma
    
a = float(input())
b = float(input())
c = float(input())

obj1 = Triangulo(a, b, c)
print(obj1.calcular_perimetro())
