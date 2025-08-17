# Project Synapse: Refactored Agentic Last-Mile Coordinator

> **🎉 REFACTORED VERSION**: This project has been completely refactored for better modularity, MCP integration, and Next.js frontend preparation!

Project Synapse is a sophisticated autonomous AI agent designed to intelligently resolve real-time, last-mile delivery disruptions. This refactored version introduces clean architecture, Model Context Protocol (MCP) support, and enhanced developer experience.

## 🚀 Quick Start

```bash
# Setup (one-time)
python scripts/setup.py
cp .env.example .env
# Add your GOOGLE_API_KEY to .env

# Run CLI
python scripts/start.py cli

# Run with MCP server
python scripts/start.py dev
```

## ✨ New Features

- **🏗️ Modular Architecture**: Clean separation into focused modules
- **🔧 MCP Integration**: FastAPI-based Model Context Protocol server
- **⚡ Enhanced Performance**: Optimized async operations
- **🧪 Comprehensive Testing**: Automated validation and demos
- **📱 Frontend Ready**: Next.js structure prepared
- **🔍 Better Debugging**: Enhanced logging and error handling

## 📁 Project Structure

```
├── src/               # Main source code
│   ├── core/          # Agent, config, prompts
│   ├── tools/         # Categorized delivery tools
│   ├── mcp/          # Model Context Protocol server/client
│   ├── utils/        # Logging and utilities
│   └── main.py       # CLI application
├── docs/             # Documentation
├── scripts/          # Utility scripts and tools
├── frontend/         # Next.js frontend (coming soon)
└── legacy/           # Original files (preserved)
```

## 🛠️ Available Tools (17 Total)

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
- `request_address_clarification` - Resolve ambiguous addresses

### ⚖️ Dispute Tools
- `initiate_mediation_flow` - Start dispute resolution
- `collect_evidence` - Gather photos and statements
- `analyze_evidence` - Determine fault
- `issue_instant_refund` - Process refunds
- `exonerate_driver` - Clear driver of fault
- `log_merchant_packaging_feedback` - Record issues

### 🔐 Verification Tools
- `verify_delivery_attempt` - GPS validation
- `initiate_qr_code_verification` - OTP alternatives

## 🌐 MCP Server

The project includes a full Model Context Protocol server:

```bash
# Start MCP server
python src/mcp/server.py
# Available at: http://localhost:8000

# API Documentation
# http://localhost:8000/docs
```

### Client Usage
```python
from src.mcp.client import SynapseMCPClient
import asyncio

async def example():
    async with SynapseMCPClient() as client:
        result = await client.call_tool(
            "get_merchant_status", 
            merchant_name="Pizza Palace"
        )
        print(result)

asyncio.run(example())
```

## 🧪 Testing & Validation

```bash
python scripts/test.py          # Comprehensive test suite
python scripts/setup.py --test  # Setup validation  
python scripts/demo.py          # Feature demonstrations
python scripts/start.py check   # Quick health check
```

## 💡 Example Scenarios

Try these in the CLI:

1. **Merchant Overload**: "Driver reports Pizza Palace is overloaded with 45-minute wait"
2. **Delivery Dispute**: "Customer complains food arrived spilled, customer ID CUST123"
3. **Address Issues**: "Driver cannot find address: Room 301, near big temple"
4. **Failed Delivery**: "Customer says driver never arrived but marked as failed"

## 🔮 Frontend (Next.js) - Coming Soon

```bash
cd frontend
npm run setup
npm run dev
```

**Planned Features:**
- 📊 Real-time delivery dashboard
- 💬 Interactive dispute resolution
- 📈 Agent analytics and monitoring
- 🔧 Tool usage visualization

## 📚 Documentation

- `docs/QUICKSTART.md` - 3-step setup guide
- `docs/REFACTORING_SUMMARY.md` - What changed and why
- `docs/PROJECT_STRUCTURE.md` - Clean project organization
- `frontend/README.md` - Frontend development guide

## 🎯 Key Capabilities

The agent autonomously handles:

- **Merchant Issues**: Overloaded restaurants, delays, alternatives
- **Customer Communication**: Notifications, chat, instructions
- **Dispute Resolution**: Evidence collection, fault analysis, refunds
- **Delivery Verification**: GPS validation, secure confirmations
- **Address Resolution**: Landmark-based navigation assistance

## 🔧 Requirements

- Python 3.9+
- Google API Key (Generative AI)
- Node.js 18+ (for frontend)

## 📄 License

MIT License - See LICENSE file for details.

---

**🚀 Ready to revolutionize delivery coordination with modular AI architecture!**

> **Migration Note**: Original files preserved in `legacy/` directory. New modular structure provides the same functionality with better organization and extensibility.