from src.phi3_engine import Phi3Engine
from src.RAG_retriever import RAGRetriever
from src.RAG_tokenizer import RAGTokenizer
from config.db import Db



def build_knowledge_base():
    tokenizer = RAGTokenizer()
    tokenizer.save_chunks()


def main():
    Db.create_tables()
    build_knowledge_base()
    engine = Phi3Engine()
    retriever = RAGRetriever()

    while True:
        query = input(">>> ")

        if query == "/q":
            break

        results = retriever.get_nearby_vectors(query)

        context = "\n\n".join(
            chunk.chunk_text for chunk in results
        )

        engine.get_response_from_model(
            question=query,
            context=context
        )


if __name__ == "__main__":
    main()