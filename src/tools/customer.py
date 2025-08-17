"""
Customer and recipient interaction tools.
"""

import random
from langchain.tools import tool


@tool
def notify_customer(customer_id: str, message: str) -> str:
    """
    Sends a notification message to a specific customer.
    Returns a confirmation that the message was sent.
    """
    return f"Notification successfully sent to customer {customer_id}."


@tool
def contact_recipient_via_chat(customer_id: str, message: str) -> str:
    """
    Initiates a chat with the recipient to ask for instructions.
    Simulates the recipient's response.
    """
    # Simulate different recipient responses
    responses = [
        "Response from recipient: 'I'm not home, please leave it with the concierge at the front desk.'",
        "Response from recipient: 'Oh no, I'm running 10 minutes late! Can the driver wait?'",
        "Response from recipient: 'I did not order anything. Please cancel this delivery.'",
        "Response from recipient: 'I'm not home right now. Can you just leave it somewhere safe?'"
    ]
    return random.choice(responses)


@tool
def suggest_safe_drop_off(address: str) -> str:
    """
    Analyzes a delivery address to suggest a safe drop-off location.
    Use this after a recipient has given permission but hasn't specified a location.
    """
    # In a real-world scenario, this might check building type, etc.
    return "Safe drop-off location found: 'Building Concierge/Reception'. Please confirm with recipient."


@tool
def find_nearby_locker(address: str) -> str:
    """
    Finds a secure parcel locker near a given address.
    Use this as a last resort if no safe drop-off is possible.
    """
    return "Found nearby secure locker: 'ParcelHub Locker #78B' at the corner of Main St and 1st Ave."


@tool
def request_address_clarification(customer_id: str, vague_address: str) -> str:
    """
    Notifies a customer that the driver cannot find their address and requests clarification.
    Simulates the customer's response with more details.
    """
    # Simulate a customer providing a helpful landmark
    return f"Customer {customer_id} has responded with clarification for '{vague_address}': 'Tell the driver to look for the big red gate near the old temple. It's the third house from there.'"
