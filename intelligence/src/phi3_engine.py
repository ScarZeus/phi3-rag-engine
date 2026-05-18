from ollama import generate


class Phi3Engine:

    def get_response_from_model(self,query):
        
        for chunk in generate('phi3', query, stream=True):
            print(chunk['response'],end='', flush=True)
        print()



