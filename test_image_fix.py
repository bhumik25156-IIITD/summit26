#!/usr/bin/env python3
"""
Test script for WiseBite image label processing with better diagnostics
"""
import requests
import io
from PIL import Image, ImageDraw

def create_test_image():
    """Create a simple test image with text"""
    # Create a white image with some text
    img = Image.new('RGB', (400, 300), color='white')
    d = ImageDraw.Draw(img)
    
    # Add some text that looks like ingredient information
    d.text((10, 10), "Ingredients:", fill='black')
    d.text((10, 40), "Sugar, Water, Salt", fill='black')
    d.text((10, 70), "Vitamin C, Citric Acid", fill='black')
    d.text((10, 100), "Allergens: Contains Peanuts", fill='red')
    
    # Save to bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def test_image_processing():
    """Test the image processing endpoint"""
    print("=" * 60)
    print("WiseBite Image Processing Test")
    print("=" * 60)
    
    # Check backend
    try:
        response = requests.get("http://localhost:8000/docs", timeout=5)
        if response.status_code != 200:
            print("❌ Backend server is not responding properly")
            return
    except Exception as e:
        print(f"❌ Cannot connect to backend: {e}")
        return

    print("✅ Backend server is running")

    # Create a test image
    print("\n📸 Creating test image...")
    test_img = create_test_image()
    print("✅ Test image created")

    # Test the image processing endpoint
    print("\n🔍 Testing /analyze-label endpoint...")
    print("   Uploading image with profile:")
    print("   - Allergies: peanuts, tree nuts")
    print("   - Diseases: diabetes")
    
    try:
        files = {'label_image': ('test_label.png', test_img, 'image/png')}
        data = {
            'allergies': 'peanuts, tree nuts',
            'diseases': 'diabetes'
        }

        response = requests.post(
            "http://localhost:8000/analyze-label",
            files=files,
            data=data,
            timeout=60
        )

        print(f"\n📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Image processed successfully!")
            result = response.json()
            print(f"\n📋 Analysis Results:")
            print(f"   Product Name: {result.get('product_name', 'N/A')}")
            print(f"   Category: {result.get('category', 'N/A')}")
            print(f"   Summary: {result.get('summary', 'N/A')[:150]}...")
            if result.get('warnings'):
                print(f"   ⚠️  Warnings: {result['warnings']}")
        else:
            print(f"❌ Error {response.status_code}:")
            try:
                error_detail = response.json().get('detail', response.text)
                print(f"   {error_detail}")
            except:
                print(f"   {response.text}")
                
    except requests.exceptions.Timeout:
        print("❌ Request timed out - API call took too long")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}: {e}")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_image_processing()
