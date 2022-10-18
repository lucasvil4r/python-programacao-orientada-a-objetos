# criar arquivo de texto

# O arquivo é criado no diretório do programa
# Se o arquivo já existe, será sobrescrito
arquivo = open("arquivo01.txt", "w", encoding="UTF-8")        # w =write

arquivo.write("Escreve uma linha\n")    # \n para pular as linhas
arquivo.write("Escreve outra linha\n")
arquivo.write(str(1.30) + "\n")         # converte numero para string

a = 100
arquivo.write(str(a) + "\n")            # escreve o conteudo de uma variável

arquivo.close()                         # fecha o arquivo
