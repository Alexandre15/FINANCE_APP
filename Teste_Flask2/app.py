from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import declarative_base, sessionmaker

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

    def __repr__(self):
        return f"Filmes[titulo='{self.titulo}', genero='{self.genero}', ano={self.ano}]"

    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano


Base.metadata.create_all(db)
# SQL

# INSERT
# data_insert = Filmes("Alita", "Ação", 2019)
# session.add(data_insert)
# session.commit()

# DELETE
# session.query(Filmes).filter(Filmes.titulo == "Batman").delete()
# session.commit()

# UPDATE


# SELECT
data = session.query(Filmes).all()
print(data)

session.close()
