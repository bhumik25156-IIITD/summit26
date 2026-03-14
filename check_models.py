import os
import google.genai as genai
from dotenv import load_dotenv

# Load your secret key
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("Your API key has access to these models:")
models = client.models.list()
for m in models:
    if 'generateContent' in m.supported_actions:
        print(m.name)