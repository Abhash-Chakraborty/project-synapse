import { NextRequest, NextResponse } from 'next/server'

const MCP_SERVER_URL = process.env.MCP_SERVER_URL || 'http://localhost:8000'

export async function GET() {
  try {
    const response = await fetch(`${MCP_SERVER_URL}/tools`)
    const data = await response.json()
    
    return NextResponse.json(data)
  } catch (error) {
    console.error('Tools API Error:', error)
    return NextResponse.json(
      { error: 'Failed to fetch tools from MCP server' },
      { status: 500 }
    )
  }
}

export async function POST(request: NextRequest) {
  try {
    const { toolName, args } = await request.json()
    
    const response = await fetch(`${MCP_SERVER_URL}/tools/${toolName}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ args })
    })

    const data = await response.json()

    if (!response.ok) {
      return NextResponse.json(
        { error: data.error || 'Tool execution failed' },
        { status: response.status }
      )
    }

    return NextResponse.json(data)
  } catch (error) {
    console.error('Tool Execution Error:', error)
    return NextResponse.json(
      { error: 'Failed to execute tool' },
      { status: 500 }
    )
  }
}
