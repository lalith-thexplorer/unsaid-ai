"""
storage.py
-----------
Responsible for lightweight, ethical storage of chat data.
Currently uses in-memory / session-safe structures.
Can be replaced with DB in production.
"""

from typing import List, Dict
import datetime


# -------------------------
# Message Structure
# -------------------------
def create_message(role: str, content: str) -> Dict:
    """
    Standard message format
    """
    return {
        "role": role,                 # 'user' or 'assistant'
        "content": content,
        "timestamp": datetime.datetime.now().isoformat()
    }


# -------------------------
# In-Memory Storage
# -------------------------
class ChatStorage:
    """
    Lightweight chat storage.
    No automatic persistence for safety reasons.
    """

    def __init__(self):
        self.messages: List[Dict] = []

    def add_message(self, role: str, content: str):
        msg = create_message(role, content)
        self.messages.append(msg)

    def get_messages(self) -> List[Dict]:
        return self.messages

    def clear(self):
        self.messages = []


# -------------------------
# Optional: Export (User-Initiated)
# -------------------------
def export_chat(messages: List[Dict]) -> str:
    """
    Export chat as readable text.
    ONLY call this with explicit user consent.
    """
    lines = []
    for msg in messages:
        role = msg["role"].upper()
        time = msg["timestamp"]
        content = msg["content"]
        lines.append(f"[{time}] {role}: {content}")

    return "\n".join(lines)
