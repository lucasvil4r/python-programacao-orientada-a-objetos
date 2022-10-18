inumerosImpares = []
inumerosPares = []

numerosPares = open('numerosPares.txt', 'r', encoding='UTF-8')

for pares in numerosPares:
    filter = pares.replace('\n', '')
    inumerosPares.append(filter)

numerosPares.close() 

numerosImpares = open('numerosImpares.txt', 'r', encoding='UTF-8')

for impares in numerosImpares:
    filter = impares.replace('\n', '')
    inumerosImpares.append(filter)

numerosImpares.close()

import numpy as np

matriz = np.concatenate((inumerosImpares, inumerosPares))
inumerosPares.sort(key=int)

arquivo = open('pares&impares.txt', 'a', encoding='UTF-8')    # a = Append

for i in matriz:
    arquivo.write(i  + '\n')

arquivo.close()     # fecha o arquivo