from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Configurações
db = create_engine('sqlite:///teste-relashionship.db')
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()


# Entidades
class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)


class Filmes(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Filmes | id: {self.id} - titulo:{self.titulo}"

    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    filmes = relationship(Filmes)

    def __repr__(self):
        return f"User | id: {self.id} - Username:{self.nome}"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


Base.metadata.create_all(db)

# Criando Usuário
user1 = User("Alexandre Fagundes", 24)
user2 = User("Vitória Arruda", 21)

# Criando filme
filme1 = Filmes("Alita", "Ação", 2019)
filme2 = Filmes("Tron", "Ficção", 2015)
filme3 = Filmes("Crepusculo", "Drama", 2013)

# Associando filme com usuário
user1.filmes.extend([filme1, filme2])
user2.filmes.append(filme3)

# Atualizar banco com as mudanças
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.filmes}=")
print(f"{user2.filmes}=")

session.close()
