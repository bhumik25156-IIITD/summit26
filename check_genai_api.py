#!/usr/bin/env python3
"""Quick test to check google-genai API types"""
import google.genai as genai

print("Available in genai module:")
print([attr for attr in dir(genai) if not attr.startswith('_')])

# Check client attributes
print("\nClient methods:")
client = genai.Client(api_key="test")
print([attr for attr in dir(client) if not attr.startswith('_')])
