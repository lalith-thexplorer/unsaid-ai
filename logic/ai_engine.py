from logic.emotion_state import detect_emotion
from logic.coping_logic import suggest_coping


def get_ai_response(message: str) -> str:
    emotion = detect_emotion(message)
    return suggest_coping(emotion.value)
