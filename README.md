# Food Detection Model API

A FastAPI-based REST API for food detection using the Qwen2.5-VL-7B-Instruct model via Hugging Face Inference API.

## Features

- Food detection from uploaded images using Qwen2.5-VL-7B-Instruct
- RESTful API endpoint
- Docker support
- Ready for GitHub Codespaces deployment
- Uses Hugging Face Inference API (more reliable than gradio_client)

## Setup

### 1. Get Your Hugging Face API Token
1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a new token with read permissions
3. Copy the token

### 2. Set Environment Variable
```bash
export HF_TOKEN="your_api_token_here"
```

Or create a `.env` file:
```bash
cp .env.example .env
# Edit .env and add your token
```

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
  "result": "Detailed food description from Qwen2.5-VL model"
}
```

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your HF_TOKEN:
```bash
export HF_TOKEN="your_token_here"
```

3. Run the server:
```bash
python server.py
```

4. The API will be available at `http://localhost:8000`

### GitHub Codespaces

1. Open this repository in GitHub Codespaces
2. Set your HF_TOKEN environment variable
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `python server.py`
5. The API will be available on the Codespaces port

## Usage Example

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@your_image.jpg"
```

## Model Information

This API uses the **Qwen/Qwen2.5-VL-7B-Instruct** model via Hugging Face Inference API for:
- Image understanding and analysis
- Food detection and description
- Detailed visual reasoning

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Hugging Face Hub
- Other dependencies listed in requirements.txt

## License

MIT License
