"""
AI Engine for Unsaid - Empathetic Chat
Uses Google Gemini API for emotional support conversations.
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# System prompt for empathetic AI
SYSTEM_PROMPT = """You are a compassionate emotional support companion named Unsaid. 

Your role:
- Listen with empathy and validate feelings
- Offer gentle coping suggestions (not prescriptions)
- Be warm, non-judgmental, and supportive
- Keep responses concise (2-3 sentences max)

Rules:
- NEVER give medical advice or diagnoses
- NEVER claim to be a therapist or doctor
- If someone mentions self-harm, gently acknowledge and suggest professional help
- Always end with an open question or supportive statement

The user's current moods are: {moods}
"""

# Crisis keywords that trigger safety overlay
CRISIS_KEYWORDS = [
    "suicide", "kill myself", "want to die", "end my life",
    "self harm", "hurt myself", "cutting", "overdose",
    "no reason to live", "better off dead"
]

def get_ai_response(user_message, mood_context=None, chat_history=None):
    """
    Generates an empathetic AI response using Gemini.
    
    Args:
        user_message: The user's input text
        mood_context: List of selected moods (optional)
        chat_history: Previous messages for context (optional)
    
    Returns:
        str: AI response text
    """
    try:
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        # Build context
        moods_str = ", ".join(mood_context) if mood_context else "not specified"
        system = SYSTEM_PROMPT.format(moods=moods_str)
        
        # Build conversation
        messages = [{"role": "user", "parts": [system + "\n\nUser: " + user_message]}]
        
        if chat_history:
            # Include recent history for context
            for msg in chat_history[-5:]:  # Last 5 messages
                messages.append(msg)
        
        response = model.generate_content(messages)
        return response.text
        
    except Exception as e:
        # Fallback responses when API unavailable
        import random
        fallback_responses = [
            "I hear you. That sounds really challenging. What's weighing on you the most right now?",
            "Thank you for sharing that with me. It takes courage to open up. How long have you been feeling this way?",
            "I'm here with you. Your feelings are valid. What would feel most supportive right now?",
            "That sounds difficult. Remember, it's okay to feel what you're feeling. What helps you when things get tough?",
            "I appreciate you trusting me with this. Would you like to tell me more about what's going on?",
        ]
        return random.choice(fallback_responses)

def detect_crisis(message):
    """
    Checks if message contains crisis-related keywords.
    
    Args:
        message: User's input text
        
    Returns:
        bool: True if crisis keywords detected
    """
    message_lower = message.lower()
    for keyword in CRISIS_KEYWORDS:
        if keyword in message_lower:
            return True
    return False

def get_coping_suggestion(mood):
    """
    Returns a gentle coping suggestion based on mood.
    """
    suggestions = {
        "Anxious": "Try taking 3 slow, deep breaths right now. 🌬️",
        "Sad": "It's okay to feel sad. Maybe write down one thing you're grateful for? 📝",
        "Tired": "Rest is important. Can you take a 5-minute break? ☕",
        "Frustrated": "Frustration is valid. Try stepping away for a moment. 🚶",
        "Numb": "Sometimes we feel nothing, and that's okay too. I'm here. 💙",
        "Calm": "That's wonderful. What's helping you feel calm today? 🌿",
        "Hopeful": "Hope is powerful. What's one thing you're looking forward to? ✨",
        "Grateful": "Gratitude is healing. What made you smile today? 😊"
    }
    return suggestions.get(mood, "Take a moment for yourself. You deserve it. 💜")
