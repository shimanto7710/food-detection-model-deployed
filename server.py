from fastapi import FastAPI, UploadFile, File
from gradio_client import Client
import uvicorn
import os

# Connect to Hugging Face Space model
client = Client("mrdbourke/qwen2.5-vl-food-detect")

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        # Run prediction using the file path directly
        result = client.predict(
            file_path,  # Pass the file path directly
            api_name="/predict"
        )
        
        # Clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)
            
        return {"result": result}
    except Exception as e:
        # Clean up temporary file on error
        if os.path.exists(file_path):
            os.remove(file_path)
        return {"error": str(e)}

if __name__ == "__main__":
    print("🚀 Starting Food Detection API Server...")
    print("🌍 Server will be available on the Codespaces forwarded port")
    print("📱 Use the Codespaces port forwarding URL for your Android app")
    uvicorn.run(app, host="0.0.0.0", port=8000)
