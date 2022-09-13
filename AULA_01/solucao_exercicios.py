# --------------------------------------------------
# Exercício 1
def somar(a, b):
    c = a + b
    return c


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
print(somar(a, b))


# --------------------------------------------------
# Exercício 2
def quadrado(a):
    b = a ** 2
    return b


a = int(input('Digite o número: '))
b = quadrado(a)
print(b)


# --------------------------------------------------
# Exercício 3
def soma_dos_quadrados(a, b):
    c = quadrado(a) + quadrado(b)
    return c


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
print(soma_dos_quadrados(a, b))


# --------------------------------------------------
# Exercício 4
def media(a, b, c):
    return (a + b + c) / 3

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))
print('Média dos números: ', media(x, y, z))

# --------------------------------------------------
# Exercício 5
def calcular_salario(salario):
    if salario > 2000:
        total = salario + salario * 7/100
    else:
        total = salario + salario * 15/100
    return total

valor = float(input('Informe o salario: '))
print('Salário Atualizado: ', calcular_salario(valor))


# --------------------------------------------------
# Exercício 6 - usando for
def soma_divisores_com_for(n):
    soma = 0
    for a in range(1, n+1):       # n = 5     a = [1,2,3,4,5]
        if n % a == 0:
            soma = soma + a
    return soma


# Exercício 6 - usando while
def soma_divisores_com_while(n):
    a = 1
    soma = 0
    while a <= n:
        if n % a == 0:
            soma = soma + a
        a = a + 1
    return soma


a = int(input('Informe um número inteiro: '))
print(soma_divisores_com_for(a))
print(soma_divisores_com_while(a))


# --------------------------------------------------
# Exercício 7 - usando for
def fatorial_com_for(n):
    f = 1
    for a in range(1, n+1):
        f = f * a
    return f


# Exercício 7 - usando while
def fatorial_com_while(n):
    a = 1
    f = 1
    while a <= n:
        f = f * a
        a = a + 1
    return f


a = int(input('Informe um número inteiro: '))
print(fatorial_com_for(a))
print(fatorial_com_while(a))

# --------------------------------------------------
