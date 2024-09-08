import requests
import base64
import json

url = "https://api.convoai.tech/v1/audio/translations"
headers = {
    "Authorization": "Bearer sk-*******************",
    "Content-Type": "application/json"
}

# Read the image and encode it in base64
with open("audio_sample.mp3", "rb") as audio_file:
    base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

# JSON payload with the model and base64 audio
data = {
    "model": "whisper-large",
    "file": base64_audio
}

# Make the POST request with the JSON payload
transcript = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response from the server
print(transcript.text)