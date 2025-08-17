"""
MCP client implementation for consuming Synapse tools via FastAPI.
"""

import asyncio
from typing import Any, Dict, List
import httpx
from ..core.config import Config
from ..utils.logger import log_info, log_error


class SynapseMCPClient:
    """Client for interacting with the Synapse MCP server."""
    
    def __init__(self, server_url: str = None):
        """Initialize the MCP client."""
        self.server_url = server_url or f"http://localhost:{Config.MCP_SERVER_PORT}"
        self.client = httpx.AsyncClient()
    
    async def call_tool(self, tool_name: str, **kwargs) -> Any:
        """
        Call a tool on the MCP server.
        
        Args:
            tool_name: Name of the tool to call
            **kwargs: Tool arguments
            
        Returns:
            Tool response
        """
        try:
            response = await self.client.post(
                f"{self.server_url}/tools/{tool_name}",
                json={"args": kwargs}
            )
            response.raise_for_status()
            result = response.json()
            
            if result.get("success", True):
                return result.get("result")
            else:
                raise Exception(result.get("error", "Unknown error"))
                
        except Exception as e:
            log_error(f"Error calling tool {tool_name}: {e}")
            raise
    
    async def get_available_tools(self) -> Dict[str, Any]:
        """Get list of available tools from the server."""
        try:
            response = await self.client.get(f"{self.server_url}/tools")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            log_error(f"Error getting available tools: {e}")
            raise
    
    async def get_agent_status(self) -> Dict[str, Any]:
        """Get the current agent status."""
        try:
            response = await self.client.get(f"{self.server_url}/resources/agent-status")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            log_error(f"Error getting agent status: {e}")
            raise
    
    async def get_server_info(self) -> Dict[str, Any]:
        """Get server information."""
        try:
            response = await self.client.get(f"{self.server_url}/")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            log_error(f"Error getting server info: {e}")
            raise
    
    async def close(self):
        """Close the client connection."""
        await self.client.aclose()
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()


# Convenience functions for common tool calls
async def quick_merchant_status(merchant_name: str) -> str:
    """Quick function to check merchant status."""
    async with SynapseMCPClient() as client:
        return await client.call_tool("get_merchant_status", merchant_name=merchant_name)


async def quick_traffic_check(route: str) -> str:
    """Quick function to check traffic."""
    async with SynapseMCPClient() as client:
        return await client.call_tool("check_traffic", route=route)


async def quick_customer_notify(customer_id: str, message: str) -> str:
    """Quick function to notify customer."""
    async with SynapseMCPClient() as client:
        return await client.call_tool("notify_customer", customer_id=customer_id, message=message)


# Synchronous wrapper functions
def sync_merchant_status(merchant_name: str) -> str:
    """Synchronous wrapper for merchant status check."""
    return asyncio.run(quick_merchant_status(merchant_name))


def sync_traffic_check(route: str) -> str:
    """Synchronous wrapper for traffic check."""
    return asyncio.run(quick_traffic_check(route))


def sync_customer_notify(customer_id: str, message: str) -> str:
    """Synchronous wrapper for customer notification."""
    return asyncio.run(quick_customer_notify(customer_id, message))
