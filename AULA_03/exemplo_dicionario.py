# EXEMPLO 1:
# Criar dicionario para armazenar um cadastro de pessoas (CPF e NOME)
cadastro = {123456: 'Paulo', 6787564: 'João', 444555: 'Maria'}

# Imprimir dicionário
print(cadastro)

# Imprimir item do dicionário (acesso pela chave)
print(cadastro[444555])

# Adicionar item no dicionario
cadastro[999999] = 'Pedro'
print(cadastro)

# Alterar item do dicionário
cadastro[444555] = 'Maria da Silva'
print(cadastro)

# Excluir item do dicionário (função pop)
cadastro.pop(123456)
print(cadastro)

# Verificar se chave existe no dicionário
if 7777777 in cadastro:
    print(cadastro[7777777])
else:
    print('O cpf nao está cadastrado')

# Percorrer o dicionario com estrutura de repetição
for a in cadastro:
    print(a)

for a in cadastro:
    print(cadastro[a])

for a in cadastro:
    print(a, cadastro[a])


# preencher dicionário com dados informados pelo usuário
cadastro = {}
for i in range(3):
    cpf = int(input('Informe o CPF: '))
    nome = input('Informe o nome: ')
    cadastro[cpf] = nome
print(cadastro)
