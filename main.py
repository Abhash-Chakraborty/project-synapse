# This script serves as the main entry point for the Project Synapse agent.
# It handles environment setup, agent initialization, and the primary execution loop.
# The core logic revolves around the LangChain AgentExecutor, which is powered by
# a custom-engineered prompt and a suite of simulated digital tools.

import os
import colorama
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.callbacks.base import BaseCallbackHandler

# Internal utilities for structured logging and color-coded output.
from logger import log_coordinator, log_final_answer, bcolors

# Import the complete suite of tools available to the agent.
from tools import (
    get_merchant_status, check_traffic, notify_customer, 
    contact_recipient_via_chat, reroute_driver, get_nearby_merchants, 
    suggest_safe_drop_off, find_nearby_locker, initiate_mediation_flow,
    collect_evidence, analyze_evidence, issue_instant_refund,
    exonerate_driver, log_merchant_packaging_feedback, 
    request_address_clarification, verify_delivery_attempt, initiate_qr_code_verification
)

# Initialize colorama to ensure cross-platform colored output in the terminal.
# autoreset=True ensures that color styles are reset after each print statement.
colorama.init(autoreset=True)

# --- ENVIRONMENT SETUP ---

# Load environment variables (specifically the API key) from a .env file.
load_dotenv()

# Security check: Ensure the Google API key is present before proceeding.
if not os.getenv("GOOGLE_API_KEY"):
    print("ERROR: GOOGLE_API_KEY not found in .env file.")
    exit()

# --- AGENT INITIALIZATION ---

# Initialize the core language model.
# Using a powerful model like gemini-1.5-pro is key for complex reasoning.
# Temperature is set to 0 for deterministic and predictable behavior during testing.
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0)

# Define the complete list of tools the agent is authorized to use.
# The agent's capabilities are entirely determined by this list.
tools = [get_merchant_status, check_traffic, notify_customer, contact_recipient_via_chat, 
         reroute_driver, get_nearby_merchants, suggest_safe_drop_off, find_nearby_locker,
         initiate_mediation_flow, collect_evidence, analyze_evidence, 
         issue_instant_refund, exonerate_driver, log_merchant_packaging_feedback, 
         request_address_clarification, verify_delivery_attempt, initiate_qr_code_verification]

# --- PROMPT ENGINEERING ---

# This system prompt defines the agent's persona, capabilities,
# and the logical rules it must follow.
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

# --- AGENT AND EXECUTOR SETUP ---

# A custom callback handler to intercept and format the agent's output.
# This class ensures a more readable CLI Output. 
class CustomCallbackHandler(BaseCallbackHandler):
    def on_agent_action(self, action, **kwargs):
        # This method is called when the agent is about to use a tool
        from logger import log_tool_call
        log_tool_call(action.tool, action.tool_input)

    def on_tool_end(self, output, **kwargs):
        # This method is called when a tool finishes running
        from logger import log_tool_output
        log_tool_output(output)

# Create the agent with the standard 'create_tool_calling_agent' LangChain constructor.
agent = create_tool_calling_agent(llm, tools, prompt)

# Create the Agent Executor, which is the runtime environment for the agent.
# It's responsible for calling tools and feeding the results back to the agent.
# `verbose=False` is set to disable LangChain's default (messy) logging.
# `callbacks` are used to hook into the agent's lifecycle for custom logging.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False,
                                callbacks=[CustomCallbackHandler()])

# --- MAIN CHATBOT LOGIC ---

def main_loop():
    """
    Main interactive loop for the chatbot.
    """
    print(f"{bcolors.HEADER}{bcolors.BOLD}Welcome to the Project Synapse Interactive CLI.")
    print(f"{bcolors.HEADER}You can describe a delivery disruption, and the agent will try to resolve it.")
    print(f"{bcolors.HEADER}Type 'exit' or 'quit' to end the session.\n")

    while True:
        # Get user input from the console.
        user_input = input(f"{bcolors.BOLD}Enter a disruption scenario: {bcolors.ENDC}")

        # Check for exit commands.
        if user_input.lower() in ["exit", "quit"]:
            print(f"{bcolors.WARNING}Ending session. Goodbye!")
            break

        # Handle empty input.
        if not user_input.strip():
            continue

        # Hand the scenario over to the agent.
        log_coordinator("Received new disruption. Handing over to the agent...")

        try:
            result = agent_executor.invoke({"input": user_input})
            log_final_answer(result['output'])
        except Exception as e:
            log_coordinator(f"An error occurred during agent execution: {e}")

        log_coordinator("Agent has completed its task and is ready for the next scenario.\n")

# --- APPLICATION ENTRY POINT ---
if __name__ == "__main__":
    main_loop()