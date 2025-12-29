from enum import Enum


class EmotionLevel(Enum):
    CALM = "calm"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


CRISIS_WORDS = [
    "suicide",
    "kill myself",
    "i want to die",
    "end my life",
    "i can't go on",
    "better off dead"
]

NEGATIVE_WORDS = [
    "sad", "hopeless", "tired", "alone",
    "worthless", "empty", "broken", "helpless"
]


def detect_emotion(message: str) -> EmotionLevel:
    """
    Detect emotional risk level from user message.
    Non-medical. Rule-based. Hackathon-safe.
    """

    if not message:
        return EmotionLevel.CALM

    msg = message.lower()

    for word in CRISIS_WORDS:
        if word in msg:
            return EmotionLevel.HIGH

    for word in NEGATIVE_WORDS:
        if word in msg:
            return EmotionLevel.MEDIUM

    return EmotionLevel.CALM
