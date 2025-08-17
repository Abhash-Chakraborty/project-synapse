# 🚀 Deployment Guide

This guide will help you deploy Project Synapse to production environments.

## 📋 Prerequisites

- Google Generative AI API Key
- Hugging Face account (for MCP server)
- Vercel account (for frontend)
- GitHub repository (for automated deployments)

## 🤖 Deploy MCP Server to Hugging Face Spaces

### Step 1: Create Hugging Face Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Configure your space:
   - **Space name**: `project-synapse-mcp` (or your preferred name)
   - **License**: MIT
   - **SDK**: Docker
   - **Visibility**: Public
   - **Hardware**: CPU basic (free tier)

### Step 2: Prepare Repository

```bash
# Clone your repository
git clone https://github.com/your-username/project-synapse.git
cd project-synapse

# Add Hugging Face remote
git remote add hf https://huggingface.co/spaces/your-username/project-synapse-mcp
```

### Step 3: Configure Environment Variables

In your Hugging Face Space settings, add:

```bash
GOOGLE_API_KEY=your_google_generative_ai_api_key
PORT=7860
```

### Step 4: Deploy

```bash
# Push to Hugging Face
git push hf main
```

Your MCP server will be available at: `https://your-username-project-synapse-mcp.hf.space`

## 🎨 Deploy Frontend to Vercel

### Step 1: Prepare Frontend

```bash
cd frontend

# Install dependencies
npm install

# Test build locally
npm run build
```

### Step 2: Deploy with Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Follow prompts and configure:
# - Project name: project-synapse-frontend
# - Framework: Next.js
# - Root directory: ./
```

### Step 3: Configure Environment Variables

In your Vercel project settings, add:

```bash
NEXT_PUBLIC_MCP_SERVER_URL=https://your-username-project-synapse-mcp.hf.space
```

### Step 4: Connect GitHub (Optional)

For automatic deployments:

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **"Import Project"**
3. Connect your GitHub repository
4. Set build configuration:
   - **Framework**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

## 🔄 Automated Deployments

### GitHub Actions Setup

1. Add secrets to your GitHub repository:
   - `HF_TOKEN`: Your Hugging Face token
   - `HF_SPACE_NAME`: Your space name (e.g., `username/project-synapse-mcp`)

2. The workflow in `.github/workflows/deploy-hf.yml` will automatically deploy to Hugging Face on pushes to main.

## 🔧 Configuration Files

### For Hugging Face Deployment:
- `Dockerfile` - Container configuration
- `.dockerignore` - Files to exclude from Docker build
- `requirements.txt` - Python dependencies
- `README_HF.md` - Hugging Face Space README

### For Vercel Deployment:
- `frontend/vercel.json` - Vercel configuration
- `frontend/.env.example` - Environment variables template
- `frontend/package.json` - Node.js dependencies

## 🌐 Access Your Deployed Application

After successful deployment:

- **MCP Server**: `https://your-username-project-synapse-mcp.hf.space`
- **API Documentation**: `https://your-username-project-synapse-mcp.hf.space/docs`
- **Frontend Dashboard**: `https://your-project-name.vercel.app`

## 🧪 Testing Deployment

### Test MCP Server

```bash
# Health check
curl https://your-username-project-synapse-mcp.hf.space/health

# List tools
curl https://your-username-project-synapse-mcp.hf.space/tools

# Test a tool
curl -X POST "https://your-username-project-synapse-mcp.hf.space/tools/get_merchant_status" \
  -H "Content-Type: application/json" \
  -d '{"merchant_name": "Pizza Palace"}'
```

### Test Frontend

1. Open your Vercel URL
2. Check dashboard loads correctly
3. Test agent interface with sample scenarios
4. Verify MCP server connection

## 🐛 Troubleshooting

### Common Issues

**MCP Server not starting:**
- Check `GOOGLE_API_KEY` is set correctly
- Verify Dockerfile builds successfully locally
- Check Hugging Face Space logs

**Frontend can't connect to MCP server:**
- Verify `NEXT_PUBLIC_MCP_SERVER_URL` environment variable
- Check CORS settings in MCP server
- Test MCP server endpoints directly

**Build failures:**
- Check all dependencies are in `requirements.txt`
- Verify Node.js version compatibility
- Check for missing environment variables

### Monitoring

- **Hugging Face**: Check Space logs and metrics
- **Vercel**: Monitor function logs and analytics
- **Frontend**: Check browser console for errors

## 🔄 Updates and Maintenance

### Updating MCP Server
```bash
git push hf main
```

### Updating Frontend
- Vercel automatically deploys on git push (if connected to GitHub)
- Or use `vercel --prod` for manual deployment

## 📚 Additional Resources

- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Vercel Documentation](https://vercel.com/docs)
- [Next.js Deployment Guide](https://nextjs.org/docs/deployment)
