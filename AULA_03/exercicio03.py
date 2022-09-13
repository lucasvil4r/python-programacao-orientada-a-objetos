def conta_vogais(texto):
    dicionario = {}
    lista_vogais = 'aeiou'

    for letra in texto:                     # percorre caracteres
        if letra in lista_vogais:           # se é uma vogal
            if letra in dicionario:         # se está no dicionario
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
    return dicionario


texto = 'faculdade de tecnologia impacta'
dicionario = conta_vogais(texto)
print(dicionario)
