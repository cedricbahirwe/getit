import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


# response = openai.ChatCompletion.create(
#     model="gpt-4", echo $VIRTUAL_ENV
# Specify the model you want to use
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "What is the capital of France?"}
#     ]
# )

# Ask a question


# def ask_question(question):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": question}
#         ]
#     )

#     answer = response['choices'][0]['message']['content']
#     return answer

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

    # Filter out empty messages and clean them up
    messages = [msg.strip() for msg in messages if msg.strip()]
    # answer = response.choices[0].text.strip()
    print("After")
    print(messages)
    return messages


# Example usage
# question = "Generate 3 commit messages based on the diffs"
# question = "Generate 3 random messages"
# answer = ask_question(question)
# print(f"Len: {len(answer)}")
# print(f"Answer: {answer}")
