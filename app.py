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
    initial_sidebar_state="expanded"
)

# -------------------------------
# Session State Initialization
# -------------------------------
if 'onboarded' not in st.session_state:
    st.session_state['onboarded'] = False
if 'checked_in' not in st.session_state:
    st.session_state['checked_in'] = False
if 'show_safety' not in st.session_state:
    st.session_state['show_safety'] = False

# -------------------------------
# Sidebar Navigation (DEV MODE)
# -------------------------------
st.sidebar.title("🧭 Unsaid Navigation")

# Dev mode toggle
dev_mode = st.sidebar.checkbox("🔧 Developer Mode", value=True)

if dev_mode:
    st.sidebar.caption("Development Navigation")
    
    SCREEN_MAP = {
        "Onboarding": onboarding_screen,
        "Mood Check-In": mood_checkin_screen,
        "Chat": chat_screen,
        "Safety Overlay": safety_screen,
        "Mood Insights": insights_screen,
        "Reflection Export": export_screen,
    }
    
    selected_screen = st.sidebar.radio(
        "Go to screen:",
        list(SCREEN_MAP.keys()),
    )
    
    # Render selected screen
    if st.session_state.get('show_safety'):
        safety_screen()
    else:
        SCREEN_MAP[selected_screen]()

else:
    # Production flow
    st.sidebar.caption("Your Journey")
    
    if st.session_state.get('show_safety'):
        # Crisis override
        st.sidebar.warning("🛡️ Safety Check")
        safety_screen()
    
    elif not st.session_state.get('onboarded'):
        st.sidebar.info("📖 Welcome")
        onboarding_screen()
    
    elif not st.session_state.get('checked_in'):
        st.sidebar.info("🎭 Check-in")
        mood_checkin_screen()
    
    else:
        # Main app navigation
        nav = st.sidebar.radio(
            "Navigate:",
            ["💬 Chat", "📊 Insights", "📄 Export"],
            label_visibility="collapsed"
        )
        
        if nav == "💬 Chat":
            chat_screen()
        elif nav == "📊 Insights":
            insights_screen()
        elif nav == "📄 Export":
            export_screen()

# -------------------------------
# Global Footer Disclaimer
# -------------------------------
st.markdown("---")
st.caption(
    "⚠️ Unsaid provides emotional support only. "
    "It does not offer medical advice, diagnosis, or treatment."
)
