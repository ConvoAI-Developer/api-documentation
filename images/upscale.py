import requests
import base64
import json

url = "https://api.convoai.tech/v1/images/upscale"
headers = {
    "Authorization": "Bearer sk-*******************",
    "Content-Type": "application/json"
}

# Read the image and encode it in base64
with open("upscale-test.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# JSON payload with the model and base64 image
data = {
    "model": "esrgan_x4",
    "imageData": base64_image,
    "resize": 2
}

# Make the POST request with the JSON payload
response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the response from the server
print(response.text)

# Save the upscaled image if the request was successful
if response.status_code == 200:
    with open("upscale-test.png", "wb") as result_file:
        result_file.write(base64.b64decode(response.json().get("image_base64", "")))