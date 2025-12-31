"""
Safety Logic for Unsaid
Handles crisis detection and safety protocols.
"""

# Crisis keywords that trigger safety intervention
CRISIS_KEYWORDS = [
    # Self-harm indicators
    "suicide", "suicidal", "kill myself", "end my life", "want to die",
    "self harm", "hurt myself", "cutting", "overdose",
    "no reason to live", "better off dead", "can't go on",
    "end it all", "give up", "no way out",
    
    # Danger indicators
    "plan to hurt", "going to hurt", "weapon", "pills",
]

# Helpline resources by region
HELPLINES = {
    "US": {
        "name": "National Suicide Prevention Lifeline",
        "number": "988",
        "text": "Text HOME to 741741"
    },
    "India": {
        "name": "iCall",
        "number": "9152987821",
        "alt": "Vandrevala Foundation: 1860-2662-345"
    },
    "UK": {
        "name": "Samaritans",
        "number": "116 123",
        "text": "Email jo@samaritans.org"
    },
    "International": {
        "name": "International Association for Suicide Prevention",
        "url": "https://www.iasp.info/resources/Crisis_Centres/"
    }
}

def detect_crisis(message):
    """
    Checks if a message contains crisis-related keywords.
    
    Args:
        message: User's input text
        
    Returns:
        dict: {is_crisis: bool, matched_keywords: list}
    """
    if not message:
        return {"is_crisis": False, "matched_keywords": []}
    
    message_lower = message.lower()
    matched = []
    
    for keyword in CRISIS_KEYWORDS:
        if keyword in message_lower:
            matched.append(keyword)
    
    return {
        "is_crisis": len(matched) > 0,
        "matched_keywords": matched
    }

def get_helplines():
    """
    Returns all available helpline resources.
    """
    return HELPLINES

def get_safety_message():
    """
    Returns a compassionate safety message.
    """
    return """
    It sounds like you might be going through something really difficult right now.
    
    **You are not alone.** There are people who care and want to help.
    
    If you're in immediate danger, please contact emergency services or a crisis helpline.
    """

def format_helpline_display():
    """
    Returns formatted helpline information for display.
    """
    lines = ["**📞 Crisis Helplines:**", ""]
    
    for region, info in HELPLINES.items():
        if 'number' in info:
            lines.append(f"**{region}**: {info['name']} - **{info['number']}**")
        if 'url' in info:
            lines.append(f"**{region}**: [{info['name']}]({info['url']})")
    
    return "\n".join(lines)
