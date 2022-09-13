alunos = {}
while len(alunos) < 5:
    try:
        ra = int(input('RA: '))
        if len(str(ra)) != 7:       # se o RA não tiver 7 dígitos
            raise ValueError
        if ra in alunos:            # se o RA já estiver cadastrado
            raise TypeError
    except ValueError:
        print("O RA está no formato incorreto")
    except TypeError:
        print("O RA já esta cadastrado")
    else:                           # else: ocorre quando não há exceção
        nome = input('Nome: ')
        alunos[ra] = nome

print(alunos)
