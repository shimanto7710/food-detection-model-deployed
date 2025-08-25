#!/bin/bash
echo "Starting Food Detection API Server..."
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Starting server on port 8000..."
python server.py
