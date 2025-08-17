#!/bin/bash

# Project Synapse Startup Script
echo "🚀 Starting Project Synapse..."

# Check if Python is available
if ! command -v python &> /dev/null
then
    echo "❌ Python is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if Node.js is available
if ! command -v node &> /dev/null
then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "🔧 Starting MCP Server..."
# Start MCP server in background
python -m src.mcp.server &
MCP_PID=$!

# Wait for MCP server to start
echo "⏳ Waiting for MCP server to start..."
sleep 5

# Test MCP server
echo "🧪 Testing MCP server..."
python test_mcp.py

echo "🌐 Starting Frontend..."
cd frontend

# Install npm dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

# Start frontend
npm run dev &
FRONTEND_PID=$!

echo "✅ Project Synapse is running!"
echo "🔗 Frontend: http://localhost:3000"
echo "🔗 MCP Server: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop all services"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $MCP_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Wait for user input
wait
