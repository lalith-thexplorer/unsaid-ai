import streamlit as st

def render():
    st.header("How are you feeling right now?")

    moods = ["😊 Happy", "😔 Sad", "⚡ Anxious", "😌 Calm", "😴 Tired", "🌈 Hopeful"]

    selected_moods = st.multiselect(
        "Select one or more moods:",
        moods,
    )

    col1, col2 = st.columns(2)
    with col1:
        st.button("Continue")
    with col2:
        st.button("Skip")
