
alunos = {}

for i in range(5):
    ra = int(input("Digite o RA: "))
    notas = []
    for j in range(3):
        n = float(input("Digite uma nota: "))
        notas.append(n)
    alunos[ra] = notas              # insere no dicionario
print(alunos)

for ra in alunos:                   # percorre dicionario
    notas = alunos[ra]
    media = sum(notas) / len(notas)
    print(ra, ":", media)
