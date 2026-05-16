from ollama import generate

def get_response_from_model(query):
    
    for chunk in generate('phi3', query, stream=True):
        print(chunk['response'],end='', flush=True)
    print()

