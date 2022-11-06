# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 6):
# Lucas Vilar - 2101658
# Gustavo R. Gatto - RA:2201041
# Gustavo Gonçalves Rodrigues - 2200601

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

# Cria a tabela FILME no banco de dados
connection.execute('''CREATE TABLE IF NOT EXISTS FILME(
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255),
                        ANO INT,
                        DURACAO INT,
                        PAIS VARCHAR(255),
                        DIRETOR VARCHAR(255),
                        AVALIACAO FLOAT)''')

# Implementar classe Filme e realizar o mapeamento da tabela


class Filme(Base):
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    ano = Column('ANO', Integer)
    duracao = Column('DURACAO', Integer)
    pais = Column('PAIS', String(255))
    diretor = Column('DIRETOR', String(255))
    avaliacao = Column('AVALIACAO', Float)

    def __init__(self, titulo, ano, duracao, pais, diretor, avaliacao):
        self.titulo = titulo
        self.ano = ano
        self.duracao = duracao
        self.pais = pais
        self.diretor = diretor
        self.avaliacao = avaliacao


# Importar filmes do file de texto movies.txt e inserir no banco de dados
# Formato do file:
# titulo;ano;duracao;pais;diretor;avaliacao
file = open('./Atividade_contínua_05/movies.txt', 'r', encoding='UTF-8')

list_movies = []
for linha in file:
    lista = linha.split(';')
    filmes = Filme(lista[0], int(lista[1]), int(lista[2]),
                   lista[3], lista[4], float(lista[5]))
    list_movies.append(filmes)
session.add_all(list_movies)
# session.commit()

# Consultar todos os filmes e ordenar pelo título
query = session.query(Filme).order_by(Filme.titulo).group_by(Filme.titulo)
for filme in query:
    print(f'{filme.titulo} | {filme.ano} | {filme.duracao} | {filme.pais} | {filme.diretor} | {filme.avaliacao}')

print('-' * 100)

# Consultar filmes do ano de 2020 e ordenar pelo título
query = session.query(Filme).filter(Filme.ano == 2020).order_by(
    Filme.titulo).group_by(Filme.titulo)
for filme in query:
    print(f'{filme.titulo} | {filme.ano} | {filme.duracao} | {filme.pais} | {filme.diretor} | {filme.avaliacao}')

print('-' * 100)

# Consultar filmes de 2019 com avaliação superior a 80 e ordenar pelo título
query = session.query(Filme).filter(Filme.ano == 2019, Filme.avaliacao > 80).order_by(
    Filme.titulo).group_by(Filme.titulo)
for filme in query:
    print(f'{filme.titulo} | {filme.ano} | {filme.duracao} | {filme.pais} | {filme.diretor} | {filme.avaliacao}')

print('-' * 100)

# Excluir todos os filmes do ano de 2020
query = session.query(Filme).filter(Filme.ano == 2020)
for filme in query:
    session.delete(filme)
    # session.commit()

print('Excluindo todos os filmes do ano de 2020')

# Exportar filmes para um arquivo de texto, ordenados pelo título e no formato:
# título;ano;duracao;país;diretor;avaliacao
query = session.query(Filme)
file = open('./Atividade_contínua_05/texto.txt', 'w', encoding='UTF-8')
for filmes in query:
    file.write(
        f'{filmes.titulo};{str(filmes.ano)};{str(filmes.duracao)};{filmes.pais};{filmes.diretor};{str(filmes.avaliacao)}\n')

print('Exportar filmes para um arquivo de texto')

file.close()
connection.close()
