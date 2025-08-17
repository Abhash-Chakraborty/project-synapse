# Project Synapse MCP Server

This directory contains documentation for the MCP server deployment.

## API Endpoints

- `GET /` - Server status and information
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation
- `GET /tools` - List all available tools
- `POST /tools/{tool_name}` - Execute specific tools

## Available Tools

The MCP server provides 17 specialized tools for delivery coordination:

### Logistics Tools (4)
- get_merchant_status
- check_traffic
- reroute_driver
- get_nearby_merchants

### Customer Tools (5)
- notify_customer
- contact_recipient_via_chat
- suggest_safe_drop_off
- find_nearby_locker
- request_address_clarification

### Dispute Tools (6)
- initiate_mediation_flow
- collect_evidence
- analyze_evidence
- issue_instant_refund
- exonerate_driver
- log_merchant_packaging_feedback

### Verification Tools (2)
- verify_delivery_attempt
- initiate_qr_code_verification

## Environment Variables

- `GOOGLE_API_KEY` - Required for LLM functionality
- `PORT` - Server port (default: 7860 for HF Spaces)
