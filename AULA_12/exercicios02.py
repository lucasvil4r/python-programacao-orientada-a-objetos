# adicionar conteúdo em arquivo de texto já existente

# abre o arquivo para adicionar informações
arquivo = open('exercicio01.txt', 'r', encoding='UTF-8')    # a = Append

# cadastra o nome e idade de 5 pessoas e adiciona no arquivo de texto
soma = 0

for conteudo in arquivo:
    conteudo = int(conteudo)
    soma += conteudo

arquivo.close()     # fecha o arquivo

print(soma)