from sentence_transformers import SentenceTransformer

class SentenceEmbeddings:

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    def get_embeddings(self,list_of_contexts):
        return self.model.encode(
            list_of_contexts
        )
    
