# INSTALAR O MÓDULO SQLALCHEMY
# Executar no terminal o comando: pip install sqlalchemy

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float, null
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)


# SCRIPT PARA CRIAR UMA NOVA TABELA NO BANCO DE DADOS
connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")


# DEFINIÇÃO DE CLASSE QUE MAPEIA UMA TABELA
class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):   # Método construtor da classe
        self.nome = nome


# DEFINIÇÃO DE CLASSE QUE MAPEIA UMA TABELA
class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, nome, paginas, autor_id):   # Método construtor da classe
        self.nome = nome
        self.paginas = paginas
        self.autor_id = autor_id


# -----------------------------------------------------------------------------
# INSERINDO DADOS NA TABELA

# Inserir um objeto

# Inserir uma lista de objetos
autor1 = Autor('Luizinho')
autor2 = Autor('Josef')

livro1 = Livro('Title1', 100, 1)
livro2 = Livro('Title2', 200, 2)

autoresLivros = [autor1, autor2, livro1, livro2]

session.add_all(autoresLivros)                  # insere os dados de todos os objetos
session.commit()


# -----------------------------------------------------------------------------
# CONSULTANDO OS DADOS DA TABELA

# Consultar todos os dados
print('-'*30)
resultado = session.query(Autor)          # Retorna uma lista de objetos
for obj in resultado:
    print(obj.id, obj.nome)


# -----------------------------------------------------------------------------
# CONSULTANDO OS DADOS DA TABELA

# Consultar todos os dados
print('-'*30)
resultado = session.query(Livro)          # Retorna uma lista de objetos
for obj in resultado:
    print(obj.id, obj.nome, obj.paginas, obj.autor_id)
