#!/usr/bin/env python3
"""
Test script for WiseBite image processing
"""
import requests
import os
from pathlib import Path

def test_image_processing():
    """Test the image processing endpoint with a sample image"""

    # Check if backend is running
    try:
        response = requests.get("http://localhost:8000/docs")
        if response.status_code != 200:
            print("❌ Backend server is not running")
            return
    except:
        print("❌ Cannot connect to backend server")
        return

    print("✅ Backend server is running")

    # Look for a test image
    test_images = [
        "/home/bhumik/Desktop/Bhumik_folder/wisebite-working/test_image.jpg",
        "/home/bhumik/Desktop/Bhumik_folder/wisebite-working/test_image.png",
        "/home/bhumik/Pictures/test_image.jpg",
        "/home/bhumik/Downloads/test_image.jpg"
    ]

    test_image = None
    for img_path in test_images:
        if os.path.exists(img_path):
            test_image = img_path
            break

    if not test_image:
        print("⚠️  No test image found. Creating a simple test...")
        # Create a simple test by calling the endpoint without an image to see error handling
        try:
            response = requests.post(
                "http://localhost:8000/analyze-label",
                data={"allergies": "", "diseases": ""},
                files={}
            )
            print(f"Response status: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error: {e}")
        return

    print(f"📸 Found test image: {test_image}")

    # Test the image processing
    try:
        with open(test_image, 'rb') as f:
            files = {'label_image': ('test_image.jpg', f, 'image/jpeg')}
            data = {'allergies': 'peanuts', 'diseases': 'diabetes'}

            print("🔍 Testing image analysis...")
            response = requests.post(
                "http://localhost:8000/analyze-label",
                files=files,
                data=data,
                timeout=30
            )

            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                print("✅ Image processed successfully!")
                print("Response preview:", response.json().get('summary', '')[:200])
            else:
                print("❌ Error processing image:")
                print(response.text)

    except Exception as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    test_image_processing()