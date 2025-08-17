# Project Synapse Frontend

A Next.js frontend for the Project Synapse AI-powered delivery coordination system.

## Features

- **Dashboard View**: Real-time monitoring of delivery coordination activities
- **Agent Interface**: Interactive interface to test AI agent scenarios
- **Tool Usage Analytics**: Visualization of tool execution and performance
- **Activity Monitor**: Live feed of system events and resolutions
- **MCP Integration**: Direct connection to Model Context Protocol server

## Setup

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Make sure the MCP server is running on `http://localhost:8000`

## Project Structure

```
frontend/
├── app/                    # Next.js app directory
│   ├── api/               # API routes for MCP integration
│   ├── globals.css        # Global styles
│   ├── layout.tsx         # Root layout
│   └── page.tsx           # Home page
├── components/            # React components
│   ├── ui/               # Base UI components
│   ├── dashboard-stats.tsx
│   ├── activity-monitor.tsx
│   ├── tool-usage-chart.tsx
│   ├── agent-interface.tsx
│   └── theme-provider.tsx
└── lib/                  # Utility functions
    └── utils.ts
```

## Usage

### Dashboard View
Monitor real-time system performance, tool usage, and delivery coordination activities.

### Agent Interface
1. Enter a delivery disruption scenario
2. Click "Execute Scenario" 
3. Watch the AI agent reason through the problem
4. See tool executions and results in real-time

### Sample Scenarios
The interface includes pre-built sample scenarios for common delivery disruptions:
- Restaurant overload situations
- Damaged package disputes  
- Recipient unavailability
- Traffic obstructions

## Integration with MCP Server

The frontend communicates with the MCP server through API routes that proxy requests:

- `/api/mcp/agent` - Agent scenario execution
- `/api/mcp/tools` - Tool management and execution

## Configuration

Environment variables in `.env.local`:
- `MCP_SERVER_URL` - URL of the MCP server (default: http://localhost:8000)
- `NEXT_PUBLIC_APP_NAME` - Application name
- `NEXT_PUBLIC_APP_DESCRIPTION` - Application description

## Planned Features

- 📊 Real-time delivery monitoring dashboard
- 💬 Interactive dispute resolution interface  
- 📈 Agent conversation history and analytics
- 🔧 Tool usage monitoring
- 🌐 WebSocket integration for live updates
- 📱 Responsive design for mobile and desktop

## Architecture

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **WebSocket** - Real-time communication with MCP server
- **Chart.js/Recharts** - Data visualization
- **Zustand/Redux** - State management

## API Integration

The frontend will connect to the MCP server running on port 8000:

```typescript
// Example API integration
const client = new SynapseMCPClient('http://localhost:8000');

// Get agent status
const status = await client.getAgentStatus();

// Call tools
const result = await client.callTool('get_merchant_status', {
  merchant_name: 'Pizza Palace'
});
```

## Development Status

🚧 **Coming Soon** - Frontend development will begin after MCP backend is stable.

Run `npm run setup` to initialize the Next.js application when ready.
