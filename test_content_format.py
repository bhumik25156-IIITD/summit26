#!/usr/bin/env python3
"""
Test to figure out the correct Content structure for google-genai
"""
import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Test 1: Simple string
print("Test 1: Simple string")
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello, what's your name?"
    )
    print("✅ String works")
    print(f"   Response: {response.text[:50]}")
except Exception as e:
    print(f"❌ String failed: {type(e).__name__}: {str(e)[:100]}")

# Test 2: List of strings
print("\nTest 2: List of strings")
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=["Hello", "What's your name?"]
    )
    print("✅ List of strings works")
    print(f"   Response: {response.text[:50]}")
except Exception as e:
    print(f"❌ List of strings failed: {type(e).__name__}: {str(e)[:100]}")

# Test 3: genai.types.Part with text
print("\nTest 3: genai.types.Part with text")
try:
    part = genai.types.Part(text="Hello")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[part]
    )
    print("✅ Part(text=) works")
    print(f"   Response: {response.text[:50]}")
except Exception as e:
    print(f"❌ Part(text=) failed: {type(e).__name__}: {str(e)[:100]}")

print("\n✓ Test complete")
