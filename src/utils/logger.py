"""
A simple utility for printing colored and formatted text to the console.
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def log_coordinator(message: str):
    """Log coordinator messages in blue."""
    print(f"{bcolors.OKBLUE}[Coordinator] {message}")

def log_agent_thought(thought: str):
    """Log agent thoughts in cyan with thinking emoji."""
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}🤔 Agent Thought:{bcolors.OKCYAN}\n{thought}")

def log_tool_call(tool_name: str, tool_input: str):
    """Log tool calls in yellow with tool emoji."""
    print(f"\n{bcolors.WARNING}{bcolors.BOLD}🛠️ Calling Tool: {tool_name}")
    if tool_input:
        print(f"{bcolors.WARNING}   Input: {tool_input}")

def log_tool_output(output: str):
    """Log tool output in yellow."""
    print(f"{bcolors.WARNING}   Output: {output}")

def log_final_answer(answer: str):
    """Log final answers in green with checkmark."""
    print(f"\n{bcolors.OKGREEN}{bcolors.BOLD}✅ Final Answer:{bcolors.OKGREEN}\n{answer}\n")

def log_error(error: str):
    """Log errors in red with error emoji."""
    print(f"\n{bcolors.FAIL}{bcolors.BOLD}❌ Error:{bcolors.FAIL}\n{error}\n")

def log_info(info: str):
    """Log general information in cyan."""
    print(f"{bcolors.OKCYAN}ℹ️ {info}")
