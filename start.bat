@echo off
echo 🚀 Starting Project Synapse...

:: Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

:: Check if Node.js is available  
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js 18+ first.
    pause
    exit /b 1
)

echo 📦 Installing Python dependencies...
pip install -r requirements.txt

echo 🔧 Starting MCP Server...
start /B python -m src.mcp.server

echo ⏳ Waiting for MCP server to start...
timeout /t 5 /nobreak >nul

echo 🧪 Testing MCP server...
python test_mcp.py

echo 🌐 Starting Frontend...
cd frontend

:: Install npm dependencies if node_modules doesn't exist
if not exist "node_modules" (
    echo 📦 Installing frontend dependencies...
    npm install
)

echo ✅ Project Synapse is starting!
echo 🔗 Frontend: http://localhost:3000
echo 🔗 MCP Server: http://localhost:8000
echo.
echo Press Ctrl+C to stop the frontend (MCP server will continue running)

:: Start frontend (this will block)
npm run dev
