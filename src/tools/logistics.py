"""
Logistics and monitoring tools for delivery coordination.
"""

import random
from langchain.tools import tool


@tool
def get_merchant_status(merchant_name: str) -> str:
    """
    Checks the current operational status and preparation time for a specific merchant.
    Returns a string describing the merchant's status.
    """
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
    traffic_conditions = [
        "Traffic is clear. No delays expected.",
        "A major accident has been reported along the route. Expect a 30-minute delay.",
        "Heavy congestion due to rush hour. Expect a 15-minute delay."
    ]
    return random.choice(traffic_conditions)


@tool
def reroute_driver(driver_id: str, new_task_description: str) -> str:
    """
    Reroutes a driver to a new task to optimize their time.
    Use this when a driver would otherwise be idle, for example, waiting for a long food prep.
    """
    return f"Driver {driver_id} has been successfully rerouted."


@tool
def get_nearby_merchants(cuisine_type: str) -> str:
    """
    Finds nearby merchants of a similar cuisine type that are operating normally.
    """
    # In a real scenario, this would query a database. Here, we simulate.
    return f"Found nearby merchants: 'Pizza Pronto' and 'Italiano Fast' are operating normally."
