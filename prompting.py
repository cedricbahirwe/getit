import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Ask a question


def ask_question(question: str) -> list[str]:
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Specify the model you want to use
        prompt=question,
        n=1,
        max_tokens=250  # Limit the response size
    )
    # Extract the response text and split into messages
    print("Before")
    print(response.choices[0].text)
    messages = response.choices[0].text.strip().split('\n')

    print("After")
    print(messages)
    return messages
