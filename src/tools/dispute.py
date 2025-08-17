"""
Dispute resolution and mediation tools.
"""

import random
from langchain.tools import tool


@tool
def initiate_mediation_flow(customer_id: str, driver_id: str) -> str:
    """
    Initiates a real-time mediation flow between a customer and a driver for a dispute.
    """
    return "Mediation flow initiated. Both parties are now in a synchronized resolution session."


@tool
def collect_evidence(customer_id: str, driver_id: str) -> str:
    """
    Guides the customer and driver to provide evidence, such as photos and answers to questions.
    Simulates the collected evidence as a structured string.
    """
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
    return f"Instant refund processed for customer {customer_id}. Reason: {reason}"


@tool
def exonerate_driver(driver_id: str, reason: str) -> str:
    """
    Clears the driver of any fault in a dispute.
    """
    return f"Driver {driver_id} has been exonerated. Reason: {reason}"


@tool
def log_merchant_packaging_feedback(merchant_name: str, feedback: str) -> str:
    """
    Logs feedback for a merchant regarding their packaging.
    """
    return f"Feedback logged for {merchant_name}: {feedback}"
