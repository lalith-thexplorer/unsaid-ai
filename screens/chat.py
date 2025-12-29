import streamlit as st

from logic.ai_engine import get_ai_response
from logic.safety_logic import detect_safety_risk
from screens import safety


# -------------------------
# Session State Init
# -------------------------
def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "show_safety_overlay" not in st.session_state:
        st.session_state.show_safety_overlay = False

    if "pending_user_message" not in st.session_state:
        st.session_state.pending_user_message = None


# -------------------------
# Continue Chat Callback
# -------------------------
def continue_chat():
    """
    Called when user chooses to continue chatting
    from the safety overlay
    """
    st.session_state.show_safety_overlay = False

    if st.session_state.pending_user_message:
        user_msg = st.session_state.pending_user_message

        ai_reply = get_ai_response(user_msg)

        st.session_state.messages.append(
            {"role": "assistant", "content": ai_reply}
        )

        st.session_state.pending_user_message = None

    st.rerun()


# -------------------------
# Chat Screen Render
# -------------------------
def render():
    init_state()

    st.title("💬 UnsAid Chat")

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # Detect safety keywords
        risk_detected = detect_safety_risk(user_input)

        if risk_detected:
            # Store message temporarily
            st.session_state.pending_user_message = user_input
            st.session_state.show_safety_overlay = True
            st.rerun()
        else:
            # Normal AI flow
            ai_reply = get_ai_response(user_input)
            st.session_state.messages.append(
                {"role": "assistant", "content": ai_reply}
            )
            st.rerun()

    # -------------------------
    # Safety Overlay
    # -------------------------
    if st.session_state.show_safety_overlay:
        safety.render(on_continue=continue_chat)
        st.stop()
