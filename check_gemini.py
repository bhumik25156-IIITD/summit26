import os
import google.genai as genai
from dotenv import load_dotenv

load_dotenv()
try:
    client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello"
    )
    print("Success: API call completed without error.")
except Exception as e:
    print(f"Error Type: {type(e).__name__}")
    print(f"Error details: {e}")
