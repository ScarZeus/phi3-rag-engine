from sqlalchemy import create_engine

class Db:

    engine = create_engine(
        "postgresql+psycopg2://postgres:password@localhost:5432/mydb",
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True
    )

    @classmethod
    def get_engine(cls):
        return cls.engine

db = Db()