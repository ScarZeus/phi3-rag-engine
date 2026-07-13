from ollama import chat

from pathlib import Path

class Phi3Engine:
    def __init__(self):
        base_path = Path(__file__).resolve().parent.parent
        prompt_path = base_path / "src" /"instructions" / "knowledge_expert.md"

        with open(prompt_path, "r", encoding="utf-8") as f:
            self.system_prompt = f.read()

    def get_response_from_model(self, question, context):
        response = chat(
            model="phi3",
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {
                    "role": "user",
                    "content": f"""
                            Context:
                                    {context}

                            Question:
                                    {question}
                    """,
                },
            ],
            stream=True,
        )

        for chunk in response:
            print(chunk["message"]["content"], end="", flush=True)

        print()