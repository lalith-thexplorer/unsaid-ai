import streamlit as st
from logic.ai_engine import get_ai_response
from logic.safety_logic import detect_safety_risk
from screens import safety


def render():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "show_safety_overlay" not in st.session_state:
        st.session_state.show_safety_overlay = False

    # Show chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Type your message…")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        if detect_safety_risk(user_input):
            st.session_state.show_safety_overlay = True

        reply = get_ai_response(user_input)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

        st.rerun()

    if st.session_state.show_safety_overlay:
        safety.render(on_continue=lambda: None)
