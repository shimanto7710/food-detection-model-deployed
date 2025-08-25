from fastapi import FastAPI, UploadFile, File
from gradio_client import Client, handle_file
import uvicorn

# Connect to Hugging Face Space model
client = Client("mrdbourke/qwen2.5-vl-food-detect")

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save uploaded file
    with open(file.filename, "wb") as f:
        f.write(await file.read())

    # Run prediction
    result = client.predict(
        input_image=handle_file(file.filename),
        api_name="/predict"
    )
    return {"result": result}

if __name__ == "__main__":
    print("🚀 Starting Food Detection API Server...")
    print("🌍 Server will be available on the Codespaces forwarded port")
    print("�� Use the Codespaces port forwarding URL for your Android app")
    uvicorn.run(app, host="0.0.0.0", port=8000)
