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

    async def process_scenario(self, scenario: str, context: dict = None) -> dict:
        """
        Process a delivery disruption scenario with detailed output.
        
        Args:
            scenario: Description of the delivery disruption
            context: Additional context for the scenario
            
        Returns:
            Dictionary with reasoning, actions, and execution results
        """
        try:
            # Capture tool executions and reasoning
            tool_executions = []
            reasoning = ""
            
            # Create a custom callback handler to capture tool usage
            class CaptureCallbackHandler(BaseCallbackHandler):
                def on_agent_action(self, action, **kwargs):
                    tool_executions.append({
                        "tool": action.tool,
                        "params": action.tool_input,
                        "reasoning": f"Using {action.tool} to resolve the scenario"
                    })
                
                def on_tool_end(self, output, **kwargs):
                    if tool_executions:
                        tool_executions[-1]["result"] = output
                        tool_executions[-1]["status"] = "success"
                
                def on_tool_error(self, error, **kwargs):
                    if tool_executions:
                        tool_executions[-1]["result"] = None
                        tool_executions[-1]["status"] = "error"
                        tool_executions[-1]["error"] = str(error)
            
            # Create temporary executor with custom callback
            temp_executor = AgentExecutor(
                agent=self.agent,
                tools=ALL_TOOLS,
                verbose=False,
                callbacks=[CaptureCallbackHandler()]
            )
            
            # Execute the scenario
            result = temp_executor.invoke({"input": scenario})
            
            return {
                "reasoning": result.get('output', 'Agent processed the scenario successfully'),
                "actions": tool_executions,
                "execution_results": tool_executions,
                "success": True
            }
            
        except Exception as e:
            log_error(f"An error occurred during agent execution: {e}")
            return {
                "reasoning": f"Error processing scenario: {str(e)}",
                "actions": [],
                "execution_results": [],
                "success": False
            }
