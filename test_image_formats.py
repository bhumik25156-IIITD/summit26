#!/usr/bin/env python3
"""
Test to figure out how to handle images in google-genai
"""
import google.genai as genai
import os
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Create a test image
img = Image.new('RGB', (100, 100), color='red')
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
img_bytes = img_byte_arr.getvalue()

# Test 1: Blob with bytes
print("Test 1: genai.types.Blob")
try:
    blob = genai.types.Blob(mime_type="image/png", data=img_bytes)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[blob, "What do you see?"]
    )
    print("✅ Blob works")
    print(f"   Response: {response.text[:50]}")
except Exception as e:
    print(f"❌ Blob failed: {type(e).__name__}: {str(e)[:150]}")

# Test 2: Part with inline_data
print("\nTest 2: genai.types.Part with inline_data")
try:
    part = genai.types.Part(
        inline_data=genai.types.Blob(mime_type="image/png", data=img_bytes)
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[part, "What do you see?"]
    )
    print("✅ Part(inline_data=Blob()) works")
    print(f"   Response: {response.text[:50]}")
except Exception as e:
    print(f"❌ Part(inline_data=Blob()) failed: {type(e).__name__}: {str(e)[:150]}")

# Test 3: Mixed list with text and blob
print("\nTest 3: Mixed list [text, Blob()]")
try:
    blob = genai.types.Blob(mime_type="image/png", data=img_bytes)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=["What do you see?", blob]
    )
    print("✅ Mixed list works")
    print(f"   Response: {response.text[:50]}")
except Exception as e:
    print(f"❌ Mixed list failed: {type(e).__name__}: {str(e)[:150]}")

print("\n✓ Test complete")
