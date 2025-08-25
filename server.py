import os
from fastapi import FastAPI, UploadFile, File
from huggingface_hub import InferenceClient
import uvicorn
import base64

app = FastAPI()

# Initialize the Inference Client
client = InferenceClient(
    provider="hyperbolic",
    api_key=os.environ.get("HF_TOKEN", "your_api_key_here")
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read the uploaded image
        image_data = await file.read()
        
        # Convert image to base64 for the API
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        image_url = f"data:image/{file.content_type};base64,{image_base64}"
        
        # Create the completion request
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-VL-7B-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What food items do you see in this image? Please describe them in detail."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url
                            }
                        }
                    ]
                }
            ],
        )
        
        result = completion.choices[0].message.content
        return {"result": result}
        
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {
        "message": "Food Detection API is running!", 
        "model": "Qwen/Qwen2.5-VL-7B-Instruct",
        "provider": "hyperbolic"
    }

if __name__ == "__main__":
    print("🚀 Starting Food Detection API Server...")
    print("🌍 Using Qwen2.5-VL-7B-Instruct model via InferenceClient")
    print("🔑 Make sure to set HF_TOKEN environment variable")
    print("📱 Use the Codespaces port forwarding URL for your Android app")
    uvicorn.run(app, host="0.0.0.0", port=8000)
