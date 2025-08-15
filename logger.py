# A simple utility for printing colored and formatted text to the console.

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
    print(f"{bcolors.OKBLUE}[Coordinator] {message}")

def log_agent_thought(thought: str):
    print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}🤔 Agent Thought:{bcolors.OKCYAN}\n{thought}")

def log_tool_call(tool_name: str, tool_input: str):
    print(f"\n{bcolors.WARNING}{bcolors.BOLD}🛠️ Calling Tool: {tool_name}")
    if tool_input:
        print(f"{bcolors.WARNING}   Input: {tool_input}")

def log_tool_output(output: str):
    print(f"{bcolors.WARNING}   Output: {output}")

def log_final_answer(answer: str):
    print(f"\n{bcolors.OKGREEN}{bcolors.BOLD}✅ Final Answer:{bcolors.OKGREEN}\n{answer}\n")