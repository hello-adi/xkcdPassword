# to make requests to dalle api based on the query string
import passw
import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

# image_prompt = passw.generate_password()[0]
try:
    response = openai.Image.create(prompt="a white siamese cat", n=1, size="256x256")
    image_url = response["data"][0]["url"]
    print(image_url)
except AuthenticationError:
    print("API keys not provided")
