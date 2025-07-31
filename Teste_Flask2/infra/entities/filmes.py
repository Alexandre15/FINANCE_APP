from infra.config.base import Base
from sqlalchemy import String, Integer, Column


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
