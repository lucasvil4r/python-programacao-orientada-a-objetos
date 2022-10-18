from asyncio.windows_events import NULL

arquivo = open('arquivo.txt', 'a', encoding='UTF-8')    # a = Append

# cadastra o nome e idade de 5 pessoas e adiciona no arquivo de texto
retorno = NULL

while (retorno != '0'):
    conteudo = input("Precione qualquer caractere para add no arquivo: ")
    arquivo.write(conteudo + '\n')
    retorno = input("Pressione 0 para encerrar ou qualquer outra tecla para continaur: ")

arquivo.close()     # fecha o arquivo
