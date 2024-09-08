import re
import os
from openai import OpenAI
from dotenv import load_dotenv
import tiktoken

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def request_commit_messages(question: str) -> list[str]:
    tokenizer = tiktoken.encoding_for_model("gpt-4")
    tokens = tokenizer.encode(question)

    print(f"Found {len(tokens)}")

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # Specify the model you want to use
        prompt=question,
        n=1,
        max_tokens=150  # Limit the response size
    )
    print(f"Received {len(response.choices)} {
          response.usage} {response.choices[0].finish_reason}")

    # Extract the response text and split into messages
    print(f"Before:\n{response.choices[0].text}")

    messages = response.choices[0].text.strip().split('\n')
    # Filter out empty messages and clean them up
    messages = [strip_non_letters(msg) for msg in messages if msg.strip()]

    print(f"After\n: {messages}")

    return messages


def strip_non_letters(s: str) -> str:
    # Use regular expressions to remove non-letter characters at the start and end
    return re.sub(r'^[^a-zA-Z]+|[^a-zA-Z]+$', '', s)
