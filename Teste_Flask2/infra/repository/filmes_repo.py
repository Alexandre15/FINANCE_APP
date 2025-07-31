from infra.config.connection import DBconect
from infra.entities.filmes import Filmes


class Repo:
    def select(self):
        with DBconect() as db:
            data = db.session.query(Filmes).all()
            return data

    def insert(self, titulo, genero, ano):
        with DBconect() as db:
            data_in = db.session.query(Filmes).insert(
                titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_in)
            db.session.commit()
