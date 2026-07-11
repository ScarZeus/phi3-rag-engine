from sqlalchemy import create_engine
from models.knowledge import Base

class Db:

    engine = create_engine(
        "postgresql+psycopg2://postgres:1234@localhost:5432/mydb",
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True
    )

    @classmethod
    def get_engine(cls):
        return cls.engine

    @classmethod
    def create_tables(cls):
        Base.metadata.create_all(cls.engine)


db = Db()