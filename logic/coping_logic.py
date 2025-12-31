"""
Coping Logic for Unsaid
Provides coping suggestions based on user's mood and context.
"""

# Coping strategies mapped to emotions
COPING_STRATEGIES = {
    "Anxious": [
        {"title": "Deep Breathing", "description": "Take 4 slow breaths: inhale 4 sec, hold 4 sec, exhale 4 sec", "emoji": "🌬️", "duration": "2 min"},
        {"title": "Grounding Exercise", "description": "Name 5 things you can see, 4 you can touch, 3 you can hear", "emoji": "🌍", "duration": "3 min"},
        {"title": "Progressive Relaxation", "description": "Tense and release each muscle group", "emoji": "💪", "duration": "5 min"},
    ],
    "Sad": [
        {"title": "Gratitude Journal", "description": "Write down 3 things you're grateful for today", "emoji": "📝", "duration": "5 min"},
        {"title": "Gentle Movement", "description": "Take a short walk or do light stretching", "emoji": "🚶", "duration": "10 min"},
        {"title": "Connect", "description": "Reach out to someone you trust", "emoji": "💬", "duration": "5 min"},
    ],
    "Tired": [
        {"title": "Power Rest", "description": "Close your eyes and rest for a few minutes", "emoji": "😴", "duration": "5 min"},
        {"title": "Hydrate", "description": "Drink a glass of water", "emoji": "💧", "duration": "1 min"},
        {"title": "Fresh Air", "description": "Step outside for fresh air and sunlight", "emoji": "☀️", "duration": "5 min"},
    ],
    "Frustrated": [
        {"title": "Step Away", "description": "Take a break from the situation", "emoji": "🚶", "duration": "5 min"},
        {"title": "Physical Release", "description": "Do 10 jumping jacks or shake it out", "emoji": "💥", "duration": "2 min"},
        {"title": "Write It Out", "description": "Journal your frustrations without filter", "emoji": "✍️", "duration": "5 min"},
    ],
    "Numb": [
        {"title": "Sensory Grounding", "description": "Hold ice, smell something strong, or taste something sour", "emoji": "🧊", "duration": "2 min"},
        {"title": "Gentle Movement", "description": "Stretch slowly and notice sensations", "emoji": "🧘", "duration": "5 min"},
        {"title": "Express Creatively", "description": "Doodle, hum, or tap a rhythm", "emoji": "🎨", "duration": "5 min"},
    ],
    "Calm": [
        {"title": "Mindful Moment", "description": "Notice this peaceful feeling and breathe", "emoji": "🧘", "duration": "3 min"},
        {"title": "Gratitude Pause", "description": "Appreciate what brought you this calm", "emoji": "🙏", "duration": "2 min"},
    ],
    "Hopeful": [
        {"title": "Vision Board", "description": "Write or draw what you're hopeful about", "emoji": "🌟", "duration": "10 min"},
        {"title": "Plan One Step", "description": "Identify one small action toward your hope", "emoji": "📋", "duration": "5 min"},
    ],
    "Grateful": [
        {"title": "Share It", "description": "Tell someone what you appreciate about them", "emoji": "💝", "duration": "3 min"},
        {"title": "Savor The Moment", "description": "Sit with this gratitude and breathe", "emoji": "✨", "duration": "2 min"},
    ],
}

def get_coping_suggestions(moods):
    """
    Returns coping strategies for the given moods.
    
    Args:
        moods: List of mood strings
        
    Returns:
        List of coping strategy dictionaries
    """
    suggestions = []
    seen_titles = set()
    
    for mood in moods:
        if mood in COPING_STRATEGIES:
            for strategy in COPING_STRATEGIES[mood]:
                if strategy['title'] not in seen_titles:
                    suggestions.append({**strategy, 'for_mood': mood})
                    seen_titles.add(strategy['title'])
    
    return suggestions[:5]  # Return top 5 unique suggestions

def get_quick_tip(mood):
    """
    Returns a quick one-liner coping tip.
    """
    tips = {
        "Anxious": "Take 3 slow, deep breaths right now. 🌬️",
        "Sad": "It's okay to feel sad. Maybe write down one thing you're grateful for? 📝",
        "Tired": "Rest is important. Can you take a 5-minute break? ☕",
        "Frustrated": "Frustration is valid. Try stepping away for a moment. 🚶",
        "Numb": "Sometimes we feel nothing, and that's okay too. I'm here. 💙",
        "Calm": "That's wonderful. What's helping you feel calm today? 🌿",
        "Hopeful": "Hope is powerful. What's one thing you're looking forward to? ✨",
        "Grateful": "Gratitude is healing. What made you smile today? 😊"
    }
    return tips.get(mood, "Take a moment for yourself. You deserve it. 💜")
