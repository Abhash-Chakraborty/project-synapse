---
title: Project Synapse MCP Server
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
app_port: 7860
---

# Project Synapse: MCP Server

This is the Model Context Protocol (MCP) server for Project Synapse, an AI-powered delivery coordination system.

## 🤖 About

Project Synapse is a sophisticated autonomous AI agent designed to intelligently resolve real-time, last-mile delivery disruptions. This MCP server provides:

- **17 Specialized Tools** for delivery coordination
- **FastAPI-based REST API** with automatic documentation
- **Real-time dispute resolution** capabilities
- **Intelligent routing and merchant management**
- **Customer communication tools**

## 🛠️ Available Tools

### 🚛 Logistics Tools
- `get_merchant_status` - Check restaurant operational status
- `check_traffic` - Analyze route conditions  
- `reroute_driver` - Optimize driver assignments
- `get_nearby_merchants` - Find alternative vendors

### 👥 Customer Tools
- `notify_customer` - Send notifications
- `contact_recipient_via_chat` - Real-time communication
- `suggest_safe_drop_off` - Secure delivery locations
- `find_nearby_locker` - Parcel locker options

### ⚖️ Dispute Tools
- `initiate_mediation_flow` - Start dispute resolution
- `collect_evidence` - Gather photos and statements
- `analyze_evidence` - Determine fault
- `issue_instant_refund` - Process refunds

### 🔐 Verification Tools
- `verify_delivery_attempt` - GPS validation
- `initiate_qr_code_verification` - OTP alternatives

## 🌐 API Endpoints

- **GET /** - Server status and information
- **GET /health** - Health check endpoint
- **GET /docs** - Interactive API documentation
- **POST /tools/{tool_name}** - Execute specific tools
- **GET /tools** - List all available tools

## 🚀 Usage

### Direct API Calls

```bash
# Check server status
curl https://your-space-name.hf.space/

# Get merchant status
curl -X POST "https://your-space-name.hf.space/tools/get_merchant_status" \
  -H "Content-Type: application/json" \
  -d '{"merchant_name": "Pizza Palace"}'

# Check traffic conditions
curl -X POST "https://your-space-name.hf.space/tools/check_traffic" \
  -H "Content-Type: application/json" \
  -d '{"origin": "123 Main St", "destination": "456 Oak Ave"}'
```

### Python Client

```python
import httpx
import asyncio

async def call_tool(tool_name: str, **kwargs):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://your-space-name.hf.space/tools/{tool_name}",
            json=kwargs
        )
        return response.json()

# Example usage
result = asyncio.run(call_tool("get_merchant_status", merchant_name="Pizza Palace"))
print(result)
```

## 🔧 Configuration

The server requires the following environment variables:

- `GOOGLE_API_KEY` - Google Generative AI API key for LLM capabilities
- `PORT` - Server port (default: 7860 for Hugging Face Spaces)

## 📚 Frontend

The complete frontend dashboard is available at: [Project Synapse Frontend](https://project-synapse-frontend.vercel.app)

## 🛡️ License

MIT License - See the full project repository for details.

## 🔗 Links

- **Frontend Dashboard**: [Vercel Deployment](https://project-synapse-frontend.vercel.app)
- **Source Code**: [GitHub Repository](https://github.com/your-username/project-synapse)
- **Documentation**: [Full API Docs](https://your-space-name.hf.space/docs)
