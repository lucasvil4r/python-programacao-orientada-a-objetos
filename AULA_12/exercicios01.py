# adicionar conteúdo em arquivo de texto já existente

# abre o arquivo para adicionar informações
arquivo = open('exercicio01.txt', 'a', encoding='UTF-8')    # a = Append

# cadastra o nome e idade de 5 pessoas e adiciona no arquivo de texto
for i in range(10):
    idade = int(input('Informe num: '))
    arquivo.write(str(idade) + '\n')

arquivo.close()     # fecha o arquivo
