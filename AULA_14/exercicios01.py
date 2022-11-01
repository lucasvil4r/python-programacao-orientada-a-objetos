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
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")

# DEFINIÇÃO DE CLASSE QUE MAPEIA UMA TABELA
class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):   # Método construtor da classe
        self.nome = nome
        self.idade = idade
        self.salario = salario

arquivo = open("funcionarios.txt", "r", encoding="UTF-8")      # r = read
conteudo = arquivo.read()
arquivo.close()   

conteudo = conteudo.split('\n')

for i in range(len(conteudo)):
    conteudo[i] = conteudo[i].split(';')

# -----------------------------------------------------------------------------
# INSERINDO DADOS NA TABELA

# Inserir um objeto

for i in range(len(conteudo)):
    func = Funcionario(conteudo[i][0], int(conteudo[i][1]), float(conteudo[i][2]))
    #session.add(func)                  # insere os dados de todos os objetos
    #session.commit()

# Realizar uma consulta na tabela de funcionários e verificar se os dados foram inseridos corretamente.
print('-'*30)
resultado = session.query(Funcionario)          # Retorna uma lista de objetos
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)     
