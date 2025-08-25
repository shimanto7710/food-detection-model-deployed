from fastapi import FastAPI, UploadFile, File
from gradio_client import Client, handle_file
import uvicorn

client = Client("mrdbourke/qwen2.5-vl-food-detect")
app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    with open(file.filename, "wb") as f:
        f.write(await file.read())
    result = client.predict(
        input_image=handle_file(file.filename),
        api_name="/predict"
    )
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
