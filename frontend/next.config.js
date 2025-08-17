/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  async rewrites() {
    return [
      {
        source: '/api/mcp/:path*',
        destination: process.env.NEXT_PUBLIC_MCP_SERVER_URL ? 
          `${process.env.NEXT_PUBLIC_MCP_SERVER_URL}/:path*` : 
          'http://localhost:8000/:path*', // Proxy to MCP server
      },
    ]
  },
}

module.exports = nextConfig
