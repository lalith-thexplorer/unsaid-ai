"""
Emotion State Logic for Unsaid
Tracks and analyzes emotional patterns.
"""

from datetime import datetime, timedelta

# Emotion categories and their properties
EMOTIONS = {
    "Anxious": {"category": "difficult", "color": "#A8DADC", "emoji": "😰"},
    "Calm": {"category": "positive", "color": "#457B9D", "emoji": "😌"},
    "Sad": {"category": "difficult", "color": "#1D3557", "emoji": "😢"},
    "Hopeful": {"category": "positive", "color": "#F1FAEE", "emoji": "🌟"},
    "Tired": {"category": "neutral", "color": "#8D99AE", "emoji": "😴"},
    "Frustrated": {"category": "difficult", "color": "#E63946", "emoji": "😤"},
    "Grateful": {"category": "positive", "color": "#2A9D8F", "emoji": "🙏"},
    "Numb": {"category": "difficult", "color": "#6C757D", "emoji": "😶"},
}

def get_emotion_info(emotion):
    """
    Returns metadata about an emotion.
    """
    return EMOTIONS.get(emotion, {"category": "neutral", "color": "#888", "emoji": "😐"})

def get_emotion_color(emotion):
    """
    Returns the color associated with an emotion.
    """
    return get_emotion_info(emotion)["color"]

def get_emotion_emoji(emotion):
    """
    Returns the emoji for an emotion.
    """
    return get_emotion_info(emotion)["emoji"]

def categorize_emotions(moods):
    """
    Categorizes a list of moods into positive, neutral, difficult.
    
    Returns:
        dict with counts for each category
    """
    categories = {"positive": 0, "neutral": 0, "difficult": 0}
    
    for mood in moods:
        info = get_emotion_info(mood)
        categories[info["category"]] += 1
    
    return categories

def get_dominant_emotion(mood_history, days=7):
    """
    Finds the most frequent emotion over the past N days.
    
    Args:
        mood_history: List of mood check-in dicts
        days: Number of days to look back
    """
    if not mood_history:
        return None
    
    cutoff = datetime.now() - timedelta(days=days)
    
    emotion_counts = {}
    for entry in mood_history:
        if entry['timestamp'] >= cutoff:
            for mood in entry['moods']:
                emotion_counts[mood] = emotion_counts.get(mood, 0) + 1
    
    if not emotion_counts:
        return None
    
    return max(emotion_counts, key=emotion_counts.get)

def get_emotional_trend(mood_history):
    """
    Analyzes if emotions are trending positive, negative, or stable.
    
    Returns:
        str: 'improving', 'declining', 'stable', or 'insufficient_data'
    """
    if len(mood_history) < 3:
        return 'insufficient_data'
    
    recent = mood_history[-3:]
    earlier = mood_history[-6:-3] if len(mood_history) >= 6 else mood_history[:3]
    
    def score_entries(entries):
        total = 0
        for entry in entries:
            categories = categorize_emotions(entry['moods'])
            total += categories['positive'] - categories['difficult']
        return total / len(entries) if entries else 0
    
    recent_score = score_entries(recent)
    earlier_score = score_entries(earlier)
    
    diff = recent_score - earlier_score
    
    if diff > 0.5:
        return 'improving'
    elif diff < -0.5:
        return 'declining'
    else:
        return 'stable'
