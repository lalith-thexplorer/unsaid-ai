CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "i want to die",
    "end my life",
    "i can't go on"
]

def is_crisis(message: str) -> bool:
    message = message.lower()
    return any(k in message for k in CRISIS_KEYWORDS)
