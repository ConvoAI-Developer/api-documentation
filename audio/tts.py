from openai import OpenAI

client = OpenAI(
    base_url="https://api.convoai.tech/v1",
    api_key="sk-*******************",
)

response = client.audio.speech.create(
    model='eleven_multilingual_v1', voice='rachel', input="Get Access to all popular AI models with ConvoAI."
)
response.stream_to_file(f"tts-audio.mp3")
