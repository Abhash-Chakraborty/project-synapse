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