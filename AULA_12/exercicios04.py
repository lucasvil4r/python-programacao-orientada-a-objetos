vogais = ['a', 'e', 'i', 'o', 'u',]

arquivo = open('arquivo.txt', 'r', encoding='UTF-8')

somaVogais = 0

for conteudo in arquivo:
    for i in range(len(conteudo)):
        if (conteudo[i] in vogais):
            somaVogais +=1

arquivo.close()     # fecha o arquivo

print(somaVogais)