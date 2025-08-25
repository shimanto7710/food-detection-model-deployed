import os
from fastapi import FastAPI, UploadFile, File
from huggingface_hub import InferenceClient
import uvicorn
import base64

app = FastAPI()

# Try to get token from Codespaces secrets first, then environment variable
HF_TOKEN = os.environ.get("HF_TOKEN") or os.environ.get("CODESPACES_SECRET_HF_TOKEN")

if not HF_TOKEN:
    print("⚠️  Warning: HF_TOKEN not found. Please set it in Codespaces secrets or environment variables.")
    HF_TOKEN = "your_api_key_here"  # Fallback

# Initialize the Inference Client
client = InferenceClient(
    provider="hyperbolic",
    api_key=HF_TOKEN
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read the uploaded image
        image_data = await file.read()
        
        # Convert image to base64 for the API
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        image_url = f"data:image/{file.content_type};base64,{image_base64}"
        
        # Create the completion request with exact format specification
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-VL-7B-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Analyze this image and identify all food items. First think about what foods you see, then provide the exact response format below.

<think>
[Describe the foods you see in the image]
</think>

```json
[
  {"bbox_2d": [x1, y1, x2, y2], "label": "Food Name"},
  {"bbox_2d": [x1, y1, x2, y2], "label": "Food Name"}
]
```

Provide bounding box coordinates [x1, y1, x2, y2] where:
- x1, y1 = top-left corner
- x2, y2 = bottom-right corner
- Coordinates should be pixel values relative to the image dimensions

Return ONLY the JSON array, no additional text."""
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
        
        # Return the complete completion object with proper error handling
        result = {
            "message": completion.choices[0].message.content,
            "model": completion.model,
            "usage": {
                "prompt_tokens": completion.usage.prompt_tokens if completion.usage else None,
                "completion_tokens": completion.usage.completion_tokens if completion.usage else None,
                "total_tokens": completion.usage.total_tokens if completion.usage else None
            } if completion.usage else None,
            "finish_reason": completion.choices[0].finish_reason
        }
        
        return result
        
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {
        "message": "Food Detection API is running!", 
        "model": "Qwen/Qwen2.5-VL-7B-Instruct",
        "provider": "hyperbolic",
        "token_set": bool(HF_TOKEN and HF_TOKEN != "your_api_key_here")
    }

if __name__ == "__main__":
    print("🚀 Starting Food Detection API Server...")
    print("🌍 Using Qwen2.5-VL-7B-Instruct model via InferenceClient")
    if HF_TOKEN and HF_TOKEN != "your_api_key_here":
        print("🔑 HF_TOKEN is set and ready!")
    else:
        print("⚠️  HF_TOKEN not found. Please set it in Codespaces secrets.")
    print("�� Use the Codespaces port forwarding URL for your Android app")
    uvicorn.run(app, host="0.0.0.0", port=8000)
