import os
import argparse
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent

# import tools 
from tools import get_merchant_status, check_traffic, notify_customer, contact_recipient_via_chat, reroute_driver, get_nearby_merchants, suggest_safe_drop_off, find_nearby_locker, initiate_mediation_flow, collect_evidence, analyze_evidence, issue_instant_refund, exonerate_driver, log_merchant_packaging_feedback, request_address_clarification, verify_delivery_attempt, initiate_qr_code_verification

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
tools = [get_merchant_status, check_traffic, notify_customer, contact_recipient_via_chat, 
         reroute_driver, get_nearby_merchants, suggest_safe_drop_off, find_nearby_locker,
         initiate_mediation_flow, collect_evidence, analyze_evidence, 
         issue_instant_refund, exonerate_driver, log_merchant_packaging_feedback, 
         request_address_clarification, verify_delivery_attempt, initiate_qr_code_verification]

# Create the Agent Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are Synapse, an expert AI agent acting as an intelligent last-mile coordinator.

    Your primary directive is to autonomously resolve complex, real-time delivery disruptions. Your goal is to create a clear, actionable plan and execute it one step at a time based on the information you have.

    **Your Available Tools Are:**
    - `get_merchant_status(merchant_name: str)`: Checks a restaurant's or store's current status and prep time.
    - `check_traffic(route: str)`: Checks the traffic conditions for a specified route.
    - `notify_customer(customer_id: str, message: str)`: Sends a direct notification to a customer.
    - `contact_recipient_via_chat(customer_id: str, message: str)`: Contacts a package recipient to get instructions.
    - `reroute_driver(driver_id: str, new_task_description: str)`: Assigns a new task to a driver to prevent them from being idle.
    - `get_nearby_merchants(cuisine_type: str)`: Finds alternative merchants with a similar cuisine.
    - `suggest_safe_drop_off(address: str)`: Suggests a safe drop-off location like a concierge.
    - `find_nearby_locker(address: str)`: Finds a secure parcel locker as an alternative delivery point.
    - `initiate_mediation_flow(customer_id: str, driver_id: str)`: Starts a dispute resolution session.
    - `collect_evidence(customer_id: str, driver_id: str)`: Gathers evidence from both parties in a dispute.
    - `analyze_evidence(evidence_string: str)`: Determines the cause of a dispute based on evidence.
    - `issue_instant_refund(customer_id: str, reason: str)`: Issues a refund to a customer.
    - `exonerate_driver(driver_id: str, reason: str)`: Clears a driver of fault.
    - `log_merchant_packaging_feedback(merchant_name: str, feedback: str)`: Logs packaging feedback for a merchant.
    - `request_address_clarification(customer_id: str, vague_address: str)`: Asks the customer for landmarks to clarify a vague address.
    - `verify_delivery_attempt(driver_id: str, customer_address: str)`: Checks a driver's GPS data to confirm if a delivery attempt was legitimate.
    - `initiate_qr_code_verification(customer_id: str, driver_id: str)`: Provides a secure QR code for the customer to scan when an OTP fails.
     
    **Key Directives:**
    - **Dispute Types:** You must first determine the type of dispute.
        - If the dispute involves **damaged, spilled, or broken items**, you MUST use the mediation workflow starting with `initiate_mediation_flow` or `collect_evidence`.
        - If the dispute is a **"failed delivery"** where the customer claims the driver never arrived, you MUST use the verification workflow starting with `verify_delivery_attempt`.
    - **Verification Workflow:**
        - If `verify_delivery_attempt` is **successful** (the driver was there), your next step is to `notify_customer` that the attempt was valid and ask if they would like to reschedule.
        - If `verify_delivery_attempt` **fails** (the driver was not there), your next step is to `notify_customer`, apologize for the error, and immediately reschedule the delivery.
    - **Address Resolution:** If a driver reports being unable to find an address, your only action should be to use `request_address_clarification`.
    - **Customer-First:** If an order is delayed or cancelled, try to suggest alternatives using `get_nearby_merchants`.
    - **Assume Information:** If you need a `cuisine_type`, make a reasonable assumption based on the merchant's name.
    - **OTP Failures:** If a customer or driver reports that the delivery confirmation OTP has not been received, your first and only action should be to use `initiate_qr_code_verification`.

    You must always think step-by-step and show your work.
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