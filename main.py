import os
import argparse
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

# load env variable (api key)
load_dotenv()

# check if api key present
if not os.getenv("GOOGLE_API_KEY"):
    print("ERROR: GOOGLE_API_KEY not found in .env file.")
    exit()

# initialise the gemini LLM
# setting temperature=0 (deterministic) for initial testing
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0)

# main application logic
def run_agent_coordinator(disruption_scenario: str):
    print(f"\n[Coordinator] Received new disruption: '{disruption_scenario}'")
    print("[Coordinator] Analyzing situation with Gemini...")

    # TODO: improve the prompt template after initial testing done
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a logistics coordinator. Acknowledge the following problem concisely."),
        ("human", "{scenario}")
    ])

    chain = prompt_template | llm
    response = chain.invoke({"scenario": disruption_scenario})

    print(f"\n[LLM Initial Analysis]: {response.content}")
    print("\n[Coordinator] Proof-of-concept is functional.")


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