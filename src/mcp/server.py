"""
FastAPI-based MCP server implementation for Project Synapse tools.
"""

from typing import Any, Dict
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ..tools.registry import ALL_TOOLS
from ..core.config import Config
from ..utils.logger import log_info, log_error

# Create FastAPI app
app = FastAPI(
    title="Project Synapse MCP Server",
    description="Model Context Protocol server for delivery coordination tools",
    version=Config.MCP_SERVER_VERSION
)

# Request models
class ToolRequest(BaseModel):
    """Request model for tool execution."""
    args: Dict[str, Any] = {}

class ToolResponse(BaseModel):
    """Response model for tool execution."""
    result: Any
    success: bool
    error: str = None

# Tool registry for quick lookup
TOOL_REGISTRY = {tool.name: tool for tool in ALL_TOOLS}

@app.get("/")
async def root():
    """Root endpoint with server information."""
    return {
        "name": Config.MCP_SERVER_NAME,
        "version": Config.MCP_SERVER_VERSION,
        "status": "active",
        "tools": len(ALL_TOOLS)
    }

@app.get("/tools")
async def list_tools():
    """List all available tools."""
    tools_info = {}
    for tool in ALL_TOOLS:
        tools_info[tool.name] = {
            "description": tool.description,
            "args": getattr(tool, 'args', {})
        }
    return tools_info

@app.post("/tools/{tool_name}")
async def call_tool(tool_name: str, request: ToolRequest) -> ToolResponse:
    """Execute a specific tool."""
    try:
        if tool_name not in TOOL_REGISTRY:
            raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
        
        tool = TOOL_REGISTRY[tool_name]
        result = tool.invoke(request.args)
        
        return ToolResponse(result=result, success=True)
    
    except Exception as e:
        log_error(f"Error executing tool {tool_name}: {e}")
        return ToolResponse(result=None, success=False, error=str(e))

@app.get("/resources/agent-status")
async def get_agent_status():
    """Get the current status of the Synapse agent."""
    return {
        "status": "active",
        "version": Config.MCP_SERVER_VERSION,
        "name": "Synapse Agent",
        "tools_loaded": len(ALL_TOOLS)
    }

@app.get("/resources/available-tools")
async def get_available_tools():
    """Get a list of all available tools."""
    tools_info = {}
    for tool in ALL_TOOLS:
        tools_info[tool.name] = {
            "description": tool.description,
            "args": getattr(tool, 'args', {})
        }
    return tools_info

# Individual tool endpoints
@app.post("/tools/get_merchant_status")
async def get_merchant_status(merchant_name: str):
    """Check merchant status."""
    from ..tools.logistics import get_merchant_status as gms
    return gms.invoke({"merchant_name": merchant_name})

@app.post("/tools/check_traffic")
async def check_traffic(route: str):
    """Check traffic conditions."""
    from ..tools.logistics import check_traffic as ct
    return ct.invoke({"route": route})

@app.post("/tools/notify_customer")
async def notify_customer(customer_id: str, message: str):
    """Send customer notification."""
    from ..tools.customer import notify_customer as nc
    return nc.invoke({"customer_id": customer_id, "message": message})

def run_mcp_server():
    """Run the MCP server."""
    log_info(f"Starting MCP server: {Config.MCP_SERVER_NAME}")
    log_info(f"Server will be available at: http://localhost:{Config.MCP_SERVER_PORT}")
    uvicorn.run(
        "src.mcp.server:app", 
        host="0.0.0.0", 
        port=Config.MCP_SERVER_PORT,
        reload=True
    )


if __name__ == "__main__":
    run_mcp_server()
