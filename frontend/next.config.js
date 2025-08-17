/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  async rewrites() {
    return [
      {
        source: '/api/mcp/:path*',
        destination: 'http://localhost:8000/:path*', // Proxy to MCP server
      },
    ]
  },
}

module.exports = nextConfig
