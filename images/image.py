from openai import OpenAI

client = OpenAI(
    base_url="https://api.convoai.tech/v1",
    api_key="sk-*******************",
)

image = client.images.generate(
    model="dall-e-3", prompt="A cute baby sea otter", size="1024x1024"
)
print(image)
