# Food Detection Model API

A FastAPI-based REST API for food detection using the Qwen2.5-VL model deployed via Hugging Face Gradio.

## Features

- Food detection from uploaded images
- RESTful API endpoint
- Docker support
- Ready for GitHub Codespaces deployment

## API Endpoints

### POST /predict
Upload an image file to get food detection results.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: image file

**Response:**
```json
{
  "result": "detected_food_items"
}
```

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python server.py
```

3. The API will be available at `http://localhost:8000`

### Docker Deployment

1. Build the image:
```bash
docker build -t food-detection-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 food-detection-api
```

### GitHub Codespaces

1. Open this repository in GitHub Codespaces
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python server.py`
4. The API will be available on the Codespaces port

## Usage Example

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_image.jpg"
```

## Model Information

This API uses the [mrdbourke/qwen2.5-vl-food-detect](https://huggingface.co/mrdbourke/qwen2.5-vl-food-detect) model for food detection.

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Gradio Client
- Other dependencies listed in requirements.txt

## License

MIT License
