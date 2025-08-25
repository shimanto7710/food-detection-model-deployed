import requests
import json

def test_api():
    """Test the food detection API"""
    url = "http://localhost:8000/predict"
    
    # Test with a sample image (you'll need to provide an actual image)
    files = {'file': open('test_image.jpg', 'rb')} if os.path.exists('test_image.jpg') else None
    
    if files:
        try:
            response = requests.post(url, files=files)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No test image found. Please add a test_image.jpg file to test the API.")

if __name__ == "__main__":
    test_api()
