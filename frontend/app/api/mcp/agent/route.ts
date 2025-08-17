import { NextRequest, NextResponse } from 'next/server'

const MCP_SERVER_URL = process.env.MCP_SERVER_URL || 'http://localhost:8000'

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    
    // Proxy the request to the MCP server
    const response = await fetch(`${MCP_SERVER_URL}/agent/execute`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body)
    })

    const data = await response.json()

    if (!response.ok) {
      return NextResponse.json(
        { error: data.error || 'MCP server error' },
        { status: response.status }
      )
    }

    return NextResponse.json(data)
  } catch (error) {
    console.error('API Error:', error)
    return NextResponse.json(
      { error: 'Failed to connect to MCP server' },
      { status: 500 }
    )
  }
}

export async function GET() {
  try {
    // Get MCP server status
    const response = await fetch(`${MCP_SERVER_URL}/`)
    const data = await response.json()
    
    return NextResponse.json(data)
  } catch (error) {
    return NextResponse.json(
      { error: 'MCP server unavailable' },
      { status: 503 }
    )
  }
}
