#!/usr/bin/env python3
"""
Quick test script to verify MCP server functionality
"""

import asyncio
import aiohttp
import json

async def test_mcp_server():
    """Test the MCP server endpoints."""
    base_url = "http://localhost:8000"
    
    async with aiohttp.ClientSession() as session:
        try:
            # Test root endpoint
            print("Testing root endpoint...")
            async with session.get(f"{base_url}/") as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✓ Server status: {data}")
                else:
                    print(f"✗ Server not responding: {response.status}")
                    return
            
            # Test tools endpoint
            print("\nTesting tools endpoint...")
            async with session.get(f"{base_url}/tools") as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✓ Available tools: {len(data)} tools loaded")
                else:
                    print(f"✗ Tools endpoint error: {response.status}")
            
            # Test agent execution
            print("\nTesting agent execution...")
            test_scenario = {
                "scenario": "A restaurant is overloaded with a 40-minute kitchen prep time. Order ID: ORD-123",
                "context": {"timestamp": "2025-08-17T12:00:00Z"}
            }
            
            async with session.post(
                f"{base_url}/agent/execute",
                json=test_scenario,
                headers={"Content-Type": "application/json"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    print(f"✓ Agent execution successful")
                    print(f"  Reasoning: {data.get('agent_reasoning', 'N/A')[:100]}...")
                    print(f"  Actions planned: {len(data.get('planned_actions', []))}")
                else:
                    print(f"✗ Agent execution error: {response.status}")
                    error_text = await response.text()
                    print(f"  Error: {error_text}")
                    
        except aiohttp.ClientConnectorError:
            print("✗ Cannot connect to MCP server. Make sure it's running on localhost:8000")
        except Exception as e:
            print(f"✗ Test failed with error: {e}")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())
