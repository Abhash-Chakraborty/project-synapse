# 📋 Deployment Checklist

Use this checklist to ensure successful deployment of Project Synapse.

## ✅ Pre-Deployment Setup

### Prerequisites
- [ ] Google Generative AI API Key obtained
- [ ] Hugging Face account created
- [ ] Vercel account created
- [ ] GitHub repository set up

### Environment Setup
- [ ] `.env` file created with `GOOGLE_API_KEY`
- [ ] Frontend `.env.local` created with MCP server URL
- [ ] All dependencies installed locally (`pip install -r requirements.txt`)
- [ ] Frontend dependencies installed (`npm install` in frontend directory)

### Local Testing
- [ ] MCP server starts successfully (`python -m src.mcp.server`)
- [ ] Frontend starts successfully (`npm run dev` in frontend directory)
- [ ] API endpoints respond correctly (test `/health`, `/tools`)
- [ ] Frontend can connect to MCP server
- [ ] Sample tool execution works

## 🤖 Hugging Face Spaces Deployment

### Space Configuration
- [ ] Hugging Face Space created with Docker SDK
- [ ] Space visibility set to Public
- [ ] License set to MIT
- [ ] README_HF.md file updated with correct URLs

### Environment Variables
- [ ] `GOOGLE_API_KEY` added to Space secrets
- [ ] `PORT=7860` configured (default for HF Spaces)

### Docker Configuration
- [ ] `Dockerfile` present and tested locally
- [ ] `.dockerignore` configured to exclude unnecessary files
- [ ] Health check endpoint (`/health`) working

### Deployment
- [ ] Git remote added for Hugging Face (`git remote add hf <space-url>`)
- [ ] Code pushed to Hugging Face (`git push hf main`)
- [ ] Space builds successfully (check build logs)
- [ ] Space is running and accessible
- [ ] API documentation available at `/docs`

### Testing
- [ ] Health check responds: `curl https://your-space.hf.space/health`
- [ ] Tools endpoint works: `curl https://your-space.hf.space/tools`
- [ ] Sample tool execution successful

## 🎨 Vercel Frontend Deployment

### Build Configuration
- [ ] `vercel.json` configuration file present
- [ ] `next.config.js` updated with standalone output
- [ ] Production build tested locally (`npm run build`)

### Environment Variables
- [ ] `NEXT_PUBLIC_MCP_SERVER_URL` set to your HF Space URL
- [ ] Optional analytics variables configured

### Deployment Options

#### Option A: Vercel CLI
- [ ] Vercel CLI installed (`npm install -g vercel`)
- [ ] Deployed using `vercel` command
- [ ] Production deployment confirmed (`vercel --prod`)

#### Option B: GitHub Integration
- [ ] Repository connected to Vercel
- [ ] Build settings configured:
  - [ ] Framework: Next.js
  - [ ] Root Directory: `frontend`
  - [ ] Build Command: `npm run build`
  - [ ] Output Directory: `.next`

### Testing
- [ ] Frontend loads successfully
- [ ] Dashboard displays correctly
- [ ] Agent interface functional
- [ ] MCP server connection working
- [ ] Sample scenarios execute properly

## 🔄 Automated Deployment (Optional)

### GitHub Actions
- [ ] `.github/workflows/deploy-hf.yml` configured
- [ ] GitHub secrets added:
  - [ ] `HF_TOKEN` (Hugging Face token)
  - [ ] `HF_SPACE_NAME` (your space name)
- [ ] Workflow triggers on push to main
- [ ] Test workflow execution

## 🌐 Post-Deployment Verification

### Connectivity
- [ ] MCP server URL accessible publicly
- [ ] Frontend URL accessible publicly
- [ ] Cross-origin requests working (CORS)
- [ ] API responses are correctly formatted

### Performance
- [ ] Page load times acceptable (<3 seconds)
- [ ] API response times reasonable (<2 seconds)
- [ ] No console errors in browser
- [ ] Health checks passing

### Documentation
- [ ] README.md updated with live demo URLs
- [ ] API documentation reflects current endpoints
- [ ] Frontend README includes deployment info
- [ ] Deployment guide accessible

## 🔧 Troubleshooting Checklist

### Common Issues
- [ ] Check API key is correctly set and valid
- [ ] Verify all required dependencies in requirements.txt
- [ ] Ensure CORS headers are properly configured
- [ ] Check environment variable names match exactly
- [ ] Verify Docker build completes without errors

### Monitoring Setup
- [ ] Error logging configured
- [ ] Health monitoring set up
- [ ] Performance metrics available
- [ ] User analytics (optional) configured

## 📚 Documentation Updates

### URLs to Update
- [ ] Main README.md with live demo links
- [ ] Frontend README.md with deployment URL
- [ ] API documentation with correct base URLs
- [ ] Environment variable examples

### Repository Maintenance
- [ ] .gitignore excludes sensitive files
- [ ] All deployment files committed
- [ ] Version tags created for releases
- [ ] License file present and accurate

## ✨ Final Verification

- [ ] Both applications deployed and accessible
- [ ] End-to-end functionality working
- [ ] All documentation updated
- [ ] Team notified of deployment URLs
- [ ] Monitoring and alerting configured

---

## 🚀 Ready for Production!

Once all items are checked, your Project Synapse deployment is ready for production use.

**Live URLs:**
- MCP Server: `https://your-username-project-synapse-mcp.hf.space`
- Frontend: `https://your-project-name.vercel.app`
- API Docs: `https://your-username-project-synapse-mcp.hf.space/docs`
