from sqlalchemy import create_engine


class Db:

    def __init__(self):

        self.engine = create_engine(
            "postgresql+psycopg2://postgres:password@localhost:5432/mydb",
            pool_size=10,
            max_overflow=20,
            pool_pre_ping=True
        )

    def get_connection(self):
        return self.engine.connect()


db = Db()