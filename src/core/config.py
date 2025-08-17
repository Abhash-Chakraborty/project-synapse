"""
Configuration settings for the Project Synapse agent.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the application."""
    
    # API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    # Model Configuration
    MODEL_NAME = "gemini-1.5-pro-latest"
    MODEL_TEMPERATURE = 0
    
    # Agent Configuration
    AGENT_NAME = "Synapse"
    AGENT_DESCRIPTION = "An expert AI agent acting as an intelligent last-mile coordinator"
    
    # MCP Configuration
    MCP_SERVER_NAME = "synapse-tools"
    MCP_SERVER_VERSION = "1.0.0"
    MCP_SERVER_PORT = int(os.getenv("PORT", 8000))
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that all required configuration is present."""
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        return True
