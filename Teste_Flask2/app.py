from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Configurações
db = create_engine('sqlite:///teste2.db')
Base = declarative_base()
Session = sessionmaker(bind=db)
session = Session()


# Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship("Atores", backref="atores", lazy="subquery")

    def __repr__(self):
        return f"{self.titulo}|Genero: {self.genero}|{self.ano}|{self.atores}"

    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano


class Atores(Base):
    __tablename__ = "atores"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey("filmes.titulo"))

    def __repr__(self):
        return f"Atores -> {self.nome} | Filme: {self.titulo_filme}"

    def __init__(self, nome, titulo_filme):
        self.nome = nome
        self.titulo_filme = titulo_filme


Base.metadata.create_all(db)
# SQL

# INSERT
data_insert = Filmes("Alita", "Ação", 2019)
session.add(data_insert)
session.commit()


data_insert = Atores("Alexandre", "Alita")
session.add(data_insert)
session.commit()

# DELETE
# session.query(Atores).filter(Atores.nome == "Alexandre").delete()
# session.commit()

# UPDATE


# SELECT
data = session.query(Atores).all()
print(data)
data2 = session.query(Filmes).all()
print(data2)
data2 = session.query(Atores).join(Filmes, Atores.titulo_filme == Filmes.titulo).with_entities(
    Atores.nome, Filmes.titulo, Filmes.genero).all()
print(data2)

session.close()
