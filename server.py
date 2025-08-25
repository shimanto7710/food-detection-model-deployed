from fastapi import FastAPI, UploadFile, File
import uvicorn
import os
import requests
import json

app = FastAPI()

# Hugging Face Space API endpoint
HF_SPACE_URL = "https://mrdbourke-qwen2-5-vl-food-detect.hf.space"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        # Prepare the file for upload
        with open(file_path, "rb") as f:
            files = {"file": f}
            
            # Make request to Hugging Face Space
            response = requests.post(
                f"{HF_SPACE_URL}/predict",
                files=files,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
            else:
                result = {"error": f"HF Space returned status {response.status_code}"}
        
        # Clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
            
        return result
        
    except Exception as e:
        # Clean up temporary file on error
        if os.path.exists(file_path):
            os.remove(file_path)
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "Food Detection API is running!", "hf_space": HF_SPACE_URL}

if __name__ == "__main__":
    print("🚀 Starting Food Detection API Server...")
    print(f"�� Connected to HF Space: {HF_SPACE_URL}")
    print("📱 Use the Codespaces port forwarding URL for your Android app")
    uvicorn.run(app, host="0.0.0.0", port=8000)
