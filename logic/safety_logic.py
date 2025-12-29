"""
safety_logic.py
---------------
Centralized safety risk detection.
Rule-based, transparent, non-medical.
"""

CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "i want to die",
    "end my life",
    "can't go on",
    "better off dead"
]


def detect_safety_risk(message: str) -> bool:
    """
    Returns True if message indicates high safety risk.
    """

    if not message:
        return False

    msg = message.lower()

    for phrase in CRISIS_KEYWORDS:
        if phrase in msg:
            return True

    return False
