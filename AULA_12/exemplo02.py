# ler arquivo de texto linha por linha

arquivo = open("arquivo.txt", "r", encoding="UTF-8")    # r = read

for linha in arquivo:   # percorre o arquivo
    print(linha)        # imprime cada linha

arquivo.close()
