from enum import Enum


class EmotionLevel(Enum):
    CALM = "calm"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


# Simple word lists (hackathon-safe)
NEGATIVE_WORDS = [
    "sad", "hopeless", "tired", "alone", "worthless",
    "empty", "broken", "helpless", "exhausted"
]

CRISIS_WORDS = [
    "suicide", "kill myself", "i want to die",
    "end my life", "i can't go on"
]


def analyze_emotion(message: str) -> EmotionLevel:
    """
    Analyze a single message and return emotional intensity.
    No diagnosis. No medical claims.
    """
    text = message.lower()

    if any(word in text for word in CRISIS_WORDS):
        return EmotionLevel.HIGH

    if any(word in text for word in NEGATIVE_WORDS):
        return EmotionLevel.MEDIUM

    return EmotionLevel.CALM


def update_emotion_state(history: list) -> EmotionLevel:
    """
    Looks at recent messages to infer emotional trend.
    history: list of user messages (strings)
    """

    if not history:
        return EmotionLevel.CALM

    recent = history[-3:]  # only recent messages
    scores = []

    for msg in recent:
        level = analyze_emotion(msg)

        if level == EmotionLevel.HIGH:
            scores.append(3)
        elif level == EmotionLevel.MEDIUM:
            scores.append(2)
        elif level == EmotionLevel.LOW:
            scores.append(1)
        else:
            scores.append(0)

    avg_score = sum(scores) / len(scores)

    if avg_score >= 2.5:
        return EmotionLevel.HIGH
    elif avg_score >= 1.5:
        return EmotionLevel.MEDIUM
    elif avg_score >= 0.5:
        return EmotionLevel.LOW
    else:
        return EmotionLevel.CALM
