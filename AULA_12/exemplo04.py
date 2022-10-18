# adicionar conteúdo em arquivo de texto já existente

# abre o arquivo para adicionar informações
arquivo = open('cadastro.txt', 'a', encoding='UTF-8')    # a = Append

# cadastra o nome e idade de 5 pessoas e adiciona no arquivo de texto
for i in range(5):
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    arquivo.write(nome + ' - ' + str(idade) + '\n')

arquivo.close()     # fecha o arquivo
