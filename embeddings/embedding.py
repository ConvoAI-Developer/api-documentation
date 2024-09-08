from openai import OpenAI

client = OpenAI(
    base_url="https://api.convoai.tech/v1",
    api_key="sk-*******************",
)

embedding = client.embeddings.create(
    model="text-embedding-3-large",
    input="AI Marketplace",
    encoding_format="float",
)
print(embedding)
