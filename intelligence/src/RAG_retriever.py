from sqlalchemy.orm import Session
from src.sentence_embeddings import SentenceEmbeddings
from config.db import Db
from models.knowledge import Knowledge


class RAGRetriever:

    def __init__(self):
        self.embedder = SentenceEmbeddings()
        self.engine = Db.get_engine()

    def get_nearby_vectors(self, query: str, top_k: int = 5):
        query_embedding = self.embedder.get_embeddings(query).tolist()

        with Session(self.engine) as session:
            results = (
                session.query(Knowledge)
                .order_by(
                    Knowledge.embedding.cosine_distance(query_embedding)
                )
                .limit(top_k)
                .all()
            )

        return results