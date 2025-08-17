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
            current_tool_index = -1
            
            # Create a custom callback handler to capture tool usage
            class CaptureCallbackHandler(BaseCallbackHandler):
                def on_agent_action(self, action, **kwargs):
                    nonlocal current_tool_index
                    current_tool_index += 1
                    tool_executions.append({
                        "tool": action.tool,
                        "params": action.tool_input,
                        "reasoning": f"Using {action.tool} to resolve the scenario",
                        "result": None,
                        "status": "pending"
                    })
                
                def on_tool_end(self, output, **kwargs):
                    nonlocal current_tool_index
                    if current_tool_index >= 0 and current_tool_index < len(tool_executions):
                        tool_executions[current_tool_index]["result"] = output
                        tool_executions[current_tool_index]["status"] = "success"
                
                def on_tool_error(self, error, **kwargs):
                    nonlocal current_tool_index
                    if current_tool_index >= 0 and current_tool_index < len(tool_executions):
                        tool_executions[current_tool_index]["result"] = f"Error: {str(error)}"
                        tool_executions[current_tool_index]["status"] = "error"
                        tool_executions[current_tool_index]["error"] = str(error)
            
            # Create temporary executor with custom callback
            temp_executor = AgentExecutor(
                agent=self.agent,
                tools=ALL_TOOLS,
                verbose=True,  # Enable verbose to help with debugging
                callbacks=[CaptureCallbackHandler()]
            )
            
            # Execute the scenario
            result = temp_executor.invoke({"input": scenario})
            
            # Post-process to ensure all tools have results
            for i, execution in enumerate(tool_executions):
                if execution["result"] is None and execution["status"] == "pending":
                    # Try to execute the tool manually to get a result
                    try:
                        tool_found = None
                        for tool in ALL_TOOLS:
                            if tool.name == execution["tool"]:
                                tool_found = tool
                                break
                        
                        if tool_found:
                            manual_result = tool_found.invoke(execution["params"])
                            tool_executions[i]["result"] = manual_result
                            tool_executions[i]["status"] = "success_manual"
                        else:
                            tool_executions[i]["result"] = "Tool not found"
                            tool_executions[i]["status"] = "error"
                    except Exception as e:
                        tool_executions[i]["result"] = f"Manual execution failed: {str(e)}"
                        tool_executions[i]["status"] = "error"
            
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
