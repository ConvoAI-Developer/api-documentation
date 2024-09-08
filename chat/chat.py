from openai import OpenAI

client = OpenAI(
    base_url="https://api.convoai.tech/v1",
    api_key="sk-*******************",
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
)
print(completion.choices[0].message)
