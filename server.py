from fastapi import FastAPI, UploadFile, File
from gradio_client import Client, handle_file
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
        # Use your exact working implementation
        result = client.predict(
            input_image=handle_file(file_path),
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

@app.get("/")
async def root():
    return {"message": "Food Detection API is running!", "model": "mrdbourke/qwen2.5-vl-food-detect"}

if __name__ == "__main__":
    print("🚀 Starting Food Detection API Server...")
    print("🌍 Connected to HF Space: mrdbourke/qwen2.5-vl-food-detect")
    print("📱 Use the Codespaces port forwarding URL for your Android app")
    uvicorn.run(app, host="0.0.0.0", port=8000)
