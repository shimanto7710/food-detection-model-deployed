#!/bin/bash
echo "🚀 Starting Food Detection API Server..."
echo "📦 Installing dependencies..."
pip install -r requirements.txt
echo "🌍 Starting server on port 8000..."
echo "📱 Your API will be available on the Codespaces forwarded port"
echo "🔗 Look for the port forwarding notification in Codespaces"
python server.py
