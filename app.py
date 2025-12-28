import streamlit as st

# Import screen render functions
from screens.onboarding import render as onboarding_screen
from screens.mood_checkin import render as mood_checkin_screen
from screens.chat import render as chat_screen
from screens.safety import render as safety_screen
from screens.insights import render as insights_screen
from screens.export import render as export_screen


# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(
    page_title="Unsaid",
    page_icon="💬",
    layout="centered",
)

# -------------------------------
# Screen Registry
# -------------------------------
SCREEN_MAP = {
    "Onboarding": onboarding_screen,
    "Mood Check-In": mood_checkin_screen,
    "Chat": chat_screen,
    "Safety Overlay": safety_screen,
    "Mood Insights": insights_screen,
    "Reflection Export": export_screen,
}

SCREEN_KEYS = list(SCREEN_MAP.keys())

# -------------------------------
# Navigation State (SOURCE OF TRUTH)
# -------------------------------
if "current_screen" not in st.session_state:
    st.session_state.current_screen = "Onboarding"

# -------------------------------
# Sidebar Navigation (DEV ONLY)
# -------------------------------
st.sidebar.title("🧭 Unsaid Navigation")
st.sidebar.caption("Development Navigation")

# Safe index resolution (prevents ValueError)
current_index = (
    SCREEN_KEYS.index(st.session_state.current_screen)
    if st.session_state.current_screen in SCREEN_KEYS
    else 0
)

selected_screen = st.sidebar.radio(
    "Go to screen:",
    SCREEN_KEYS,
    index=current_index,
)

# Sync sidebar → app navigation
if selected_screen != st.session_state.current_screen:
    st.session_state.current_screen = selected_screen
    st.rerun()

# -------------------------------
# Main Screen Renderer
# -------------------------------
SCREEN_MAP[st.session_state.current_screen]()

# -------------------------------
# Global Footer Disclaimer
# -------------------------------
st.markdown("---")
st.caption(
    "⚠️ Unsaid provides emotional support only. "
    "It does not offer medical advice, diagnosis, or treatment."
)
