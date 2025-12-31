"""
Storage Logic for Unsaid
Handles session-based data persistence.

NOTE: Unsaid is privacy-first. We use Streamlit session_state for data storage.
This means:
- Data is only stored in browser memory during the session
- Data is NOT sent to any server
- Data is cleared when the browser tab is closed
- No cookies, no tracking, no persistence
"""

import streamlit as st
from datetime import datetime

def init_storage():
    """
    Initializes all session state variables.
    Call this at app startup.
    """
    defaults = {
        'onboarded': False,
        'checked_in': False,
        'show_safety': False,
        'trusted_contact': None,
        'selected_moods': [],
        'mood_history': [],
        'chat_messages': [],
        'export_notes': '',
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

def save_mood_checkin(moods):
    """
    Saves a mood check-in to history.
    
    Args:
        moods: List of mood strings
    """
    if 'mood_history' not in st.session_state:
        st.session_state['mood_history'] = []
    
    st.session_state['mood_history'].append({
        'timestamp': datetime.now(),
        'moods': moods
    })
    
    st.session_state['selected_moods'] = moods

def get_mood_history():
    """
    Returns the full mood history.
    """
    return st.session_state.get('mood_history', [])

def get_current_moods():
    """
    Returns the currently selected moods.
    """
    return st.session_state.get('selected_moods', [])

def save_chat_message(role, content):
    """
    Saves a chat message.
    
    Args:
        role: 'user' or 'assistant'
        content: Message text
    """
    if 'chat_messages' not in st.session_state:
        st.session_state['chat_messages'] = []
    
    st.session_state['chat_messages'].append({
        'role': role,
        'content': content,
        'timestamp': datetime.now()
    })

def get_chat_messages():
    """
    Returns all chat messages.
    """
    return st.session_state.get('chat_messages', [])

def save_trusted_contact(contact):
    """
    Saves the trusted contact.
    """
    st.session_state['trusted_contact'] = contact

def get_trusted_contact():
    """
    Returns the trusted contact.
    """
    return st.session_state.get('trusted_contact')

def clear_all_data():
    """
    Clears all user data from session.
    """
    st.session_state['mood_history'] = []
    st.session_state['chat_messages'] = []
    st.session_state['selected_moods'] = []
    st.session_state['export_notes'] = ''
    st.session_state['checked_in'] = False

def get_session_summary():
    """
    Returns a summary of the current session for export.
    """
    return {
        'mood_history': get_mood_history(),
        'chat_messages': get_chat_messages(),
        'trusted_contact': get_trusted_contact(),
        'generated_at': datetime.now()
    }
