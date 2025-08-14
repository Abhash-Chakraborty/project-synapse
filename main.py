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
    ("system", "You are an intelligent logistics coordinator for a delivery service. "
               "You must be concise and proactive. Your goal is to solve delivery "
               "disruptions by using the tools available to you. Show your reasoning "
               "at each step."),
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