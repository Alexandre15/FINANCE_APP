from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBconect:
    def __init__(self) -> None:
        self.__connection_string = 'sqlite:///teste2.db'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        db = create_engine(self.__connection_string)
        return db

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()