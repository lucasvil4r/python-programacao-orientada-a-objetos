# ARQUIVO DE TESTE
# Esse arquivo não deve ser alterado

from ac03 import Escola, Casa, Pessoa, Professor, Disciplina, Torneio, Aluno

try:
    # Criação do objeto Escola
    hogwarts = Escola("Escola de Magia e Bruxaria de Hogwarts")
    assert hogwarts.nome == 'Escola de Magia e Bruxaria de Hogwarts'
    print('CORRETO: Criação do objeto Escola')
except Exception:
    print('ERRO...: Criação do objeto Escola')

try:
    # Criação dos objetos Casa
    grifinoria = Casa("Grifinória", "Leão")
    sonserina = Casa("Sonserina", "Serpente")
    corvinal = Casa("Corvinal", "Corvo")
    lufalufa = Casa("Lufa-Lufa", "Texugo")
    assert sonserina.nome == "Sonserina"
    assert sonserina.animal == "Serpente"
    print('CORRETO: Criação dos objetos Casa')
except Exception:
    print('ERRO...: Criação dos objetos Casa')

try:
    # Criação dos objetos Disciplina
    herbologia = Disciplina("Herbologia", "Ervas, Fungos e Árvores Mágicas")
    transfiguracao = Disciplina("Transfiguracao", "Transfiguração Humana")
    pocoes = Disciplina("Poções", "Poções Simples, Poções Avançadas")
    defesa = Disciplina("Defesa", "Maldições, Dementadores, Feitiços verbais")
    assert defesa.nome == "Defesa"
    assert herbologia.ementa == "Ervas, Fungos e Árvores Mágicas"
    print('CORRETO: Criação dos objetos Disciplina')
except Exception:
    print('ERRO...: Criação dos objetos Disciplina')

try:
    # Teste da classe Pessoa
    pessoa1 = Pessoa("Ana Paula", "19351004")
    assert pessoa1.nome == "Ana Paula"
    assert pessoa1.nascimento == "19351004"
    print('CORRETO: Criação do objeto Pessoa')
except Exception:
    print('ERRO...: Criação do objeto Pessoa')

try:
    # Criação dos objetos Professor
    minerva = Professor("Minerva McGonagall", "19351004")
    filio = Professor("Fílio Flitwick", "19301017")
    pomona = Professor("Pomona Sprout", "19410515")
    severo = Professor("Severo Snape", "19600109")
    assert minerva.nome == "Minerva McGonagall"
    assert severo.nascimento == "19600109"
    print('CORRETO: Criação dos objetos Professor')
except Exception:
    print('ERRO...: Criação dos objetos Professor')

try:
    # Criação dos objetos Aluno
    draco = Aluno("Draco Malfoy", "19800605", "puro-sangue")
    ernesto = Aluno("Ernesto Macmillan", "19800901", "puro-sangue")
    hermione = Aluno("Hermione Granger", "19790919", "trouxa")
    harry = Aluno("Harry Potter", "19800731", "mestiço")
    luna = Aluno("Luna Lovegood", "19810213", "puro-sangue")
    assert luna.nome == "Luna Lovegood"
    assert luna.nascimento == "19810213"
    assert draco.tipo == "puro-sangue"
    print('CORRETO: Criação dos objetos Aluno')
except Exception:
    print('ERRO...: Criação dos objetos Aluno')

try:
    # Criação do objeto Torneio
    torneio = Torneio(sonserina, grifinoria)
    assert torneio.casa1.nome == "Sonserina"
    assert torneio.casa2.nome == "Grifinória"
    print('CORRETO: Criação do objeto Torneio')
except Exception:
    print('ERRO...: Criação do objeto Torneio')

try:
    # Inclui as casas na escola
    hogwarts.incluir_casa(grifinoria)
    hogwarts.incluir_casa(sonserina)
    hogwarts.incluir_casa(corvinal)
    hogwarts.incluir_casa(lufalufa)
    assert len(hogwarts.casas) == 4
    print('CORRETO: Inclui as casas na escola')
except Exception:
    print('ERRO...: Inclui as casas na escola')

try:
    # Definição dos diretores das casas (set_diretor e get_diretor)
    grifinoria.set_diretor(minerva)
    sonserina.set_diretor(severo)
    corvinal.set_diretor(filio)
    lufalufa.set_diretor(pomona)
    assert grifinoria.get_diretor().nome == "Minerva McGonagall"
    print('CORRETO: Definição dos diretores das casas')
except Exception:
    print('ERRO...: Definição dos diretores das casas')

try:
    # Definicao dos monitores das casas (set_monitor e get_monitor)
    grifinoria.set_monitor(hermione)
    sonserina.set_monitor(draco)
    corvinal.set_monitor(ernesto)
    lufalufa.set_monitor(luna)
    assert grifinoria.get_monitor().nome == "Hermione Granger"
    print('CORRETO: Definicao dos monitores das casas')
except Exception:
    print('ERRO...: Definicao dos monitores das casas')

try:
    # Definição das casas dos alunos
    draco.set_casa(sonserina)
    ernesto.set_casa(corvinal)
    hermione.set_casa(grifinoria)
    harry.set_casa(grifinoria)
    luna.set_casa(lufalufa)
    assert draco.casa.nome == "Sonserina"
    print('CORRETO: Definição das casas dos alunos')
except Exception:
    print('ERRO...: Definição das casas dos alunos')

try:
    # Definicao dos professores das disciplinas
    severo.incluir_disciplina(defesa)
    severo.incluir_disciplina(transfiguracao)
    minerva.incluir_disciplina(herbologia)
    filio.incluir_disciplina(transfiguracao)
    pomona.incluir_disciplina(pocoes)
    assert severo.disciplinas[1].nome == "Transfiguracao"
    print('CORRETO: Definicao dos professores das disciplinas')
except Exception:
    print('ERRO...: Definicao dos professores das disciplinas')

try:
    # Definição das disciplinas dos alunos
    harry.incluir_disciplina(herbologia)
    harry.incluir_disciplina(defesa)
    hermione.incluir_disciplina(herbologia)
    hermione.incluir_disciplina(transfiguracao)
    hermione.incluir_disciplina(defesa)
    draco.incluir_disciplina(transfiguracao)
    draco.incluir_disciplina(defesa)
    ernesto.incluir_disciplina(pocoes)
    ernesto.incluir_disciplina(defesa)
    luna.incluir_disciplina(defesa)
    assert len(harry.disciplinas) == 2
    assert len(hermione.disciplinas) == 3
    assert len(draco.disciplinas) == 2
    assert len(luna.disciplinas) == 1
    assert len(ernesto.disciplinas) == 2
    assert harry.disciplinas[0].nome == "Herbologia"
    print('CORRETO: Definição das disciplinas dos alunos')
except Exception:
    print('ERRO...: Definição das disciplinas dos alunos')

try:
    # Inclusão de triunfos e mau_feitos dos alunos
    harry.incluir_triunfo(3)
    harry.incluir_mau_feito(1)
    draco.incluir_mau_feito(2)
    draco.incluir_triunfo(1)
    hermione.incluir_triunfo(4)
    harry.incluir_triunfo(2)
    assert hermione.get_triunfos() == 4
    assert draco.get_mau_feitos() == 2
    print('CORRETO: Inclusão de triunfos e mau_feitos dos alunos')
except Exception:
    print('ERRO...: Inclusão de triunfos e mau_feitos dos alunos')

try:
    # Marcação de pontos no torneio de quadribol
    torneio.marcar_ponto(sonserina, 2)
    torneio.marcar_ponto(grifinoria, 1)
    torneio.marcar_ponto(grifinoria, 3)
    torneio.marcar_ponto(sonserina, 1)
    assert torneio.get_pontos_casa1() == 3
    assert torneio.get_pontos_casa2() == 4
    print('CORRETO: Marcação de pontos no torneio de quadribol')
except Exception:
    print('ERRO...: Marcação de pontos no torneio de quadribol')
