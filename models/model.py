from openai import OpenAI

client = OpenAI(
    base_url="https://api.convoai.tech/v1",
    api_key="sk-*******************",
)

model_list = client.models.list()
print(model_list)
