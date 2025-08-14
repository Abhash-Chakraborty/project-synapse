# tools.py
import random
from langchain.tools import tool

@tool
def get_merchant_status(merchant_name: str) -> str:
    """
    Checks the current operational status and preparation time for a specific merchant.
    Returns a string describing the merchant's status.
    """
    print(f"--- Calling Tool: get_merchant_status with merchant: {merchant_name} ---")
    statuses = {
        "overloaded": "The merchant is overloaded. Estimated prep time is 40 minutes.",
        "normal": "The merchant is operating normally. Estimated prep time is 15 minutes.",
        "closed": "The merchant is currently closed."
    }
    chosen_status = random.choice(list(statuses.keys()))
    return statuses[chosen_status]

@tool
def check_traffic(route: str) -> str:
    """
    Checks the traffic conditions for a given route.
    Returns a string describing the traffic situation.
    """
    print(f"--- Calling Tool: check_traffic for route: {route} ---")
    traffic_conditions = [
        "Traffic is clear. No delays expected.",
        "A major accident has been reported along the route. Expect a 30-minute delay.",
        "Heavy congestion due to rush hour. Expect a 15-minute delay."
    ]
    return random.choice(traffic_conditions)

@tool
def notify_customer(customer_id: str, message: str) -> str:
    """
    Sends a notification message to a specific customer.
    Returns a confirmation that the message was sent.
    """
    print(f"--- Calling Tool: notify_customer for customer: {customer_id} ---")
    print(f"Message: '{message}'")
    return f"Notification successfully sent to customer {customer_id}."

@tool
def contact_recipient_via_chat(customer_id: str, message: str) -> str:
    """
    Initiates a chat with the recipient to ask for instructions.
    Simulates the recipient's response.
    """
    print(f"--- Calling Tool: contact_recipient_via_chat for customer: {customer_id} ---")
    print(f"Message to recipient: '{message}'")
    
    # Simulate different recipient responses
    responses = [
        "Response from recipient: 'I'm not home, please leave it with the concierge at the front desk.'",
        "Response from recipient: 'Oh no, I'm running 10 minutes late! Can the driver wait?'",
        "Response from recipient: 'I did not order anything. Please cancel this delivery.'",
        "Response from recipient: 'I'm not home right now. Can you just leave it somewhere safe?'"
    ]
    return random.choice(responses)

@tool
def reroute_driver(driver_id: str, new_task_description: str) -> str:
    """
    Reroutes a driver to a new task to optimize their time.
    Use this when a driver would otherwise be idle, for example, waiting for a long food prep.
    """
    print(f"--- Calling Tool: reroute_driver for driver: {driver_id} ---")
    print(f"New task: '{new_task_description}'")
    return f"Driver {driver_id} has been successfully rerouted."

@tool
def get_nearby_merchants(cuisine_type: str) -> str:
    """
    Finds nearby merchants of a similar cuisine type that are operating normally.
    """
    print(f"--- Calling Tool: get_nearby_merchants for cuisine: {cuisine_type} ---")
    # In a real scenario, this would query a database. Here, we simulate.
    return f"Found nearby merchants: 'Pizza Pronto' and 'Italiano Fast' are operating normally."

@tool
def suggest_safe_drop_off(address: str) -> str:
    """
    Analyzes a delivery address to suggest a safe drop-off location.
    Use this after a recipient has given permission but hasn't specified a location.
    """
    print(f"--- Calling Tool: suggest_safe_drop_off for address: {address} ---")
    # In a real-world scenario, this might check building type, etc.
    return "Safe drop-off location found: 'Building Concierge/Reception'. Please confirm with recipient."

@tool
def find_nearby_locker(address: str) -> str:
    """
    Finds a secure parcel locker near a given address.
    Use this as a last resort if no safe drop-off is possible.
    """
    print(f"--- Calling Tool: find_nearby_locker for address: {address} ---")
    return "Found nearby secure locker: 'ParcelHub Locker #78B' at the corner of Main St and 1st Ave."