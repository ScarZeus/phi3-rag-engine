from src.phi3_engine import Phi3Engine

def main():
    query = input('>>> ')
    while query != '/q':
        engine = Phi3Engine()
        response = engine.get_response_from_model(query)
        query = input('>>> ')   
if __name__ == '__main__':
    main()

