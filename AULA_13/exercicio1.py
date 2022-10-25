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
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")


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

# -----------------------------------------------------------------------------
# INSERINDO DADOS NA TABELA

# Inserir um objeto
func1 = Funcionario('Zezinho', 20, 1700)
func2 = Funcionario('Luizinho', 22, 1250)
func3 = Funcionario('Huguinho', 22, 2200)
lista = [func1, func2, func3]
session.add_all(lista)                  # insere os dados de todos os objetos
session.commit()

# -----------------------------------------------------------------------------
# CONSULTANDO OS DADOS DA TABELA

# Realizar uma consulta na tabela de funcionários e verificar se os dados foram inseridos corretamente.
print('-'*30)
resultado = session.query(Funcionario)          # Retorna uma lista de objetos
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)

# -----------------------------------------------------------------------------
# CONSULTANDO OS DADOS DA TABELA

# Realizar uma consulta na tabela de todos os funcionários com salário superior a R$ 1.500,00.
print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for obj in resultado:
    print(obj.id, obj.nome, obj.idade, obj.salario)
