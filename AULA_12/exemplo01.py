# ler arquivo de texto

# o arquivo já deve existir
# procura no diretório do programa
arquivo = open("arquivo.txt", "r", encoding="UTF-8")      # r = read

# copia todo o conteúdo do arquivo para uma única variável string
a = arquivo.read()

print(a)    # imprime o conteúdo do arquivo no terminal

arquivo.close()                         # Fecha o arquivo
