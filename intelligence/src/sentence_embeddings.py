from sentence_transformers import SentenceTransformer

class SentenceEmbeddings:
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    @classmethod
    def get_embeddings(cls, texts):
        return cls.model.encode(texts)