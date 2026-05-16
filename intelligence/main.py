from src.load_model import get_response_from_model

def main():
    query = input('>>> ')
    while query != '/q':
        response = get_response_from_model(query)
        query = input('>>> ')

if __name__ == '__main__':
    main()

