"""
Main agent implementation and callback handlers.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.callbacks.base import BaseCallbackHandler

from .config import Config
from .prompts import create_agent_prompt
from ..tools.registry import ALL_TOOLS
from ..utils.logger import log_tool_call, log_tool_output, log_error


class CustomCallbackHandler(BaseCallbackHandler):
    """Custom callback handler to intercept and format the agent's output."""
    
    def on_agent_action(self, action, **kwargs):
        """Called when the agent is about to use a tool."""
        log_tool_call(action.tool, action.tool_input)

    def on_tool_end(self, output, **kwargs):
        """Called when a tool finishes running."""
        log_tool_output(output)


class SynapseAgent:
    """Main Synapse agent for delivery coordination."""
    
    def __init__(self):
        """Initialize the agent with configuration and tools."""
        Config.validate()
        
        # Initialize the language model
        self.llm = ChatGoogleGenerativeAI(
            model=Config.MODEL_NAME,
            temperature=Config.MODEL_TEMPERATURE
        )
        
        # Create the agent prompt
        self.prompt = create_agent_prompt()
        
        # Create the agent
        self.agent = create_tool_calling_agent(
            self.llm, 
            ALL_TOOLS, 
            self.prompt
        )
        
        # Create the agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=ALL_TOOLS,
            verbose=False,
            callbacks=[CustomCallbackHandler()]
        )
    
    def process_scenario(self, scenario: str) -> str:
        """
        Process a delivery disruption scenario.
        
        Args:
            scenario: Description of the delivery disruption
            
        Returns:
            Agent's response and resolution
        """
        try:
            result = self.agent_executor.invoke({"input": scenario})
            return result['output']
        except Exception as e:
            log_error(f"An error occurred during agent execution: {e}")
            raise
