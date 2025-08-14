import os
import argparse
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

# import tools 
from tools import get_merchant_status, check_traffic, notify_customer, contact_recipient_via_chat

# load env variable (api key)
load_dotenv()

# check if api key present
if not os.getenv("GOOGLE_API_KEY"):
    print("ERROR: GOOGLE_API_KEY not found in .env file.")
    exit()

# initialise the gemini LLM
# setting temperature=0 (deterministic) for initial testing
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0)

# define list of tools
tools = [get_merchant_status, check_traffic, notify_customer, contact_recipient_via_chat]

# Create the Agent Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are Project Synapse, an expert AI agent acting as an intelligent last-mile coordinator.

    Your primary directive is to autonomously resolve complex, real-time delivery disruptions.
    When you receive a scenario, you must:
    1.  **Reason Step-by-Step**: Analyze the situation to understand the core problem.
    2.  **Select a Tool**: Choose the most appropriate tool from your available toolkit to gather more information or take action.
    3.  **Act**: Execute the chosen tool with the correct parameters.
    4.  **Observe**: Analyze the output from the tool.
    5.  **Repeat**: Continue this "Reason, Act, Observe" loop until the disruption is fully resolved.

    **Your Available Tools Are:**
    - `get_merchant_status(merchant_name: str)`: Checks a restaurant's or store's current status and prep time. Use this for issues related to order preparation.
    - `check_traffic(route: str)`: Checks the traffic conditions for a specified route. Use this for potential travel delays.
    - `notify_customer(customer_id: str, message: str)`: Sends a direct notification to a customer. Use this to communicate updates, delays, or resolutions.
    - `contact_recipient_via_chat(customer_id: str, message: str)`: Contacts a package recipient to get instructions when they are unavailable. Use this for delivery-point issues.

    You must always think step-by-step and show your work. When you have a final answer or a complete resolution plan, state it clearly.
    """),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# creating agent
agent = create_tool_calling_agent(llm, tools, prompt)

# create agent executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# main application logic
def run_agent_coordinator(disruption_scenario: str):
    print(f"\n[Coordinator] Received new disruption. Handing over to the agent...")
    print(f"Scenario: '{disruption_scenario}'")

    # Invoke the agent executor with the scenario
    result = agent_executor.invoke({"input": disruption_scenario})

    print("\n[Coordinator] Agent has completed its task.")
    print(f"[Final Answer]: {result['output']}")

# command line parsing setup. 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Project Synapse: Agentic Last-Mile Coordinator"
    )
    parser.add_argument(
        "scenario",
        type=str,
        help="A string describing the last-mile delivery disruption.",
    )
    args = parser.parse_args()
    run_agent_coordinator(args.scenario)