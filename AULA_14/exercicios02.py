# INSTALAR O MÓDULO SQLALCHEMY
# Executar no terminal o comando: pip install sqlalchemy

# IMPORTAR MÓDULOS
from sqlalchemy import create_engine, Column, Integer, String, Float, null
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)

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

# Realizar uma consulta na tabela de funcionários e verificar se os dados foram inseridos corretamente.
resultado = session.query(Funcionario.nome, Funcionario.salario, func.min(Funcionario.salario))
for obj in resultado:
    print(obj.nome, obj.salario)
    