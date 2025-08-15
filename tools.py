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

# --- Dispute Resolution Tools ---

@tool
def initiate_mediation_flow(customer_id: str, driver_id: str) -> str:
    """
    Initiates a real-time mediation flow between a customer and a driver for a dispute.
    """
    print(f"--- Calling Tool: initiate_mediation_flow between {customer_id} and {driver_id} ---")
    return "Mediation flow initiated. Both parties are now in a synchronized resolution session."

@tool
def collect_evidence(customer_id: str, driver_id: str) -> str:
    """
    Guides the customer and driver to provide evidence, such as photos and answers to questions.
    Simulates the collected evidence as a structured string.
    """
    print(f"--- Calling Tool: collect_evidence from {customer_id} and {driver_id} ---")
    # Simulate different evidence outcomes
    evidence_scenarios = [
        "{'customer_photo': 'spilled_drink.jpg', 'driver_photo': 'intact_bag_seal.jpg', 'customer_statement': 'The seal was intact when I received it.', 'driver_statement': 'The bag was sealed by the merchant.'}",
        "{'customer_photo': 'crushed_box.jpg', 'driver_photo': 'torn_bag.jpg', 'customer_statement': 'The bag was already torn.', 'driver_statement': 'The bag was flimsy and tore when I picked it up.'}"
    ]
    return f"Evidence collected: {random.choice(evidence_scenarios)}"

@tool
def analyze_evidence(evidence_string: str) -> str:
    """
    Analyzes the collected evidence to determine the likely cause of the dispute.
    """
    print(f"--- Calling Tool: analyze_evidence ---")
    # Convert to lower case for case-insensitive matching
    evidence = evidence_string.lower()
    
    is_seal_intact = "'seal was intact'" in evidence or "'intact_bag_seal.jpg'" in evidence
    is_spilled = "'spilled_drink.jpg'" in evidence
    is_bag_torn = "'torn_bag.jpg'" in evidence

    if is_seal_intact and is_spilled:
        return "Conclusion: Merchant packaging fault. The bag seal was intact, but the contents were damaged."
    elif is_bag_torn:
        return "Conclusion: Driver mishandling fault. The packaging itself was damaged during transit."
    else:
        return "Conclusion: Inconclusive. Requires manual review."

@tool
def issue_instant_refund(customer_id: str, reason: str) -> str:
    """
    Issues an instant refund to the customer.
    """
    print(f"--- Calling Tool: issue_instant_refund for {customer_id} ---")
    return f"Instant refund processed for customer {customer_id}. Reason: {reason}"

@tool
def exonerate_driver(driver_id: str, reason: str) -> str:
    """
    Clears the driver of any fault in a dispute.
    """
    print(f"--- Calling Tool: exonerate_driver for {driver_id} ---")
    return f"Driver {driver_id} has been exonerated. Reason: {reason}"

@tool
def log_merchant_packaging_feedback(merchant_name: str, feedback: str) -> str:
    """
    Logs feedback for a merchant regarding their packaging.
    """
    print(f"--- Calling Tool: log_merchant_packaging_feedback for {merchant_name} ---")
    return f"Feedback logged for {merchant_name}: {feedback}"

@tool
def request_address_clarification(customer_id: str, vague_address: str) -> str:
    """
    Notifies a customer that the driver cannot find their address and requests clarification.
    Simulates the customer's response with more details.
    """
    print(f"--- Calling Tool: request_address_clarification for customer {customer_id} ---")
    # Simulate a customer providing a helpful landmark
    return f"Customer {customer_id} has responded with clarification for '{vague_address}': 'Tell the driver to look for the big red gate near the old temple. It's the third house from there.'"

@tool
def verify_delivery_attempt(driver_id: str, customer_address: str) -> str:
    """
    Verifies if a driver was physically at a customer's address by checking GPS data.
    Use this when a customer disputes a 'failed delivery' notification.
    """
    print(f"--- Calling Tool: verify_delivery_attempt for driver {driver_id} ---")
    # Simulate that the driver sometimes fakes the attempt
    if random.choice([True, True, False]): # 2 in 3 chance of being a real attempt
        return f"Verification successful: Driver {driver_id}'s GPS data confirms they were at or near '{customer_address}'."
    else:
        return f"Verification FAILED: Driver {driver_id}'s GPS data does NOT show them near '{customer_address}' at the time of the marked attempt."
    
@tool
def initiate_qr_code_verification(customer_id: str, driver_id: str) -> str:
    """
    Initiates a secure, in-app QR code verification when an OTP fails.
    The driver's app displays a QR code for the customer to scan.
    """
    print(f"--- Calling Tool: initiate_qr_code_verification for customer {customer_id} ---")
    return f"QR code for in-app verification has been sent to driver {driver_id}'s device. Customer {customer_id} must scan it to confirm the delivery."