"""
Verification and security tools.
"""

import random
from langchain.tools import tool


@tool
def verify_delivery_attempt(driver_id: str, customer_address: str) -> str:
    """
    Verifies if a driver was physically at a customer's address by checking GPS data.
    Use this when a customer disputes a 'failed delivery' notification.
    """
    # Simulate that the driver sometimes fakes the attempt
    if random.choice([True, True, False]):  # 2 in 3 chance of being a real attempt
        return f"Verification successful: Driver {driver_id}'s GPS data confirms they were at or near '{customer_address}'."
    else:
        return f"Verification FAILED: Driver {driver_id}'s GPS data does NOT show them near '{customer_address}' at the time of the marked attempt."


@tool
def initiate_qr_code_verification(customer_id: str, driver_id: str) -> str:
    """
    Initiates a secure, in-app QR code verification when an OTP fails.
    The driver's app displays a QR code for the customer to scan.
    """
    return f"QR code for in-app verification has been sent to driver {driver_id}'s device. Customer {customer_id} must scan it to confirm the delivery."
