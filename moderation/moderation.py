from openai import OpenAI

client = OpenAI(
    base_url="https://api.convoai.tech/v1",
    api_key="sk-*******************",
)

moderation = client.moderations.create(model="text-moderation-stable", input="I want to kill them.")
print(moderation)
