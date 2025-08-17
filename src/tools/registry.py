"""
Tool registry to collect all available tools.
"""

from .logistics import get_merchant_status, check_traffic, reroute_driver, get_nearby_merchants
from .customer import (
    notify_customer, contact_recipient_via_chat, suggest_safe_drop_off, 
    find_nearby_locker, request_address_clarification
)
from .dispute import (
    initiate_mediation_flow, collect_evidence, analyze_evidence, 
    issue_instant_refund, exonerate_driver, log_merchant_packaging_feedback
)
from .verification import verify_delivery_attempt, initiate_qr_code_verification

# All available tools
ALL_TOOLS = [
    # Logistics tools
    get_merchant_status,
    check_traffic,
    reroute_driver,
    get_nearby_merchants,
    
    # Customer interaction tools
    notify_customer,
    contact_recipient_via_chat,
    suggest_safe_drop_off,
    find_nearby_locker,
    request_address_clarification,
    
    # Dispute resolution tools
    initiate_mediation_flow,
    collect_evidence,
    analyze_evidence,
    issue_instant_refund,
    exonerate_driver,
    log_merchant_packaging_feedback,
    
    # Verification tools
    verify_delivery_attempt,
    initiate_qr_code_verification,
]

__all__ = [
    'ALL_TOOLS',
    'get_merchant_status',
    'check_traffic',
    'reroute_driver',
    'get_nearby_merchants',
    'notify_customer',
    'contact_recipient_via_chat',
    'suggest_safe_drop_off',
    'find_nearby_locker',
    'request_address_clarification',
    'initiate_mediation_flow',
    'collect_evidence',
    'analyze_evidence',
    'issue_instant_refund',
    'exonerate_driver',
    'log_merchant_packaging_feedback',
    'verify_delivery_attempt',
    'initiate_qr_code_verification',
]
