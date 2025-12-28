import streamlit as st

PRIMARY_MOODS = {
    "😊 Happy": ["😄 Excited", "🫶 Grateful", "😌 Calm", "💪 Motivated", "😇 Content"],
    "😔 Sad": ["😢 Lonely", "😞 Low", "💔 Hurt", "😟 Hopeless"],
    "😐 Neutral": ["😶 Numb", "🤔 Thoughtful", "😑 Meh"],
    "⚡ Anxious": ["😰 Stressed", "🤯 Overwhelmed", "😬 Nervous"],
    "😴 Tired": ["🥱 Burnt Out", "😪 Sleepy", "🪫 Drained"],
    "🌈 Other": ["😡 Angry", "🤩 Inspired", "🥳 Playful"]
}

def init_mood_state():
    if "primary_mood" not in st.session_state:
        st.session_state.primary_mood = None
    if "selected_sub_moods" not in st.session_state:
        st.session_state.selected_sub_moods = set()

def set_primary_mood(mood):
    # single-select behavior
    st.session_state.primary_mood = mood
    st.session_state.selected_sub_moods.clear()
    st.rerun()  # force immediate UI sync

def toggle_sub_mood(mood):
    # multi-select behavior
    if mood in st.session_state.selected_sub_moods:
        st.session_state.selected_sub_moods.remove(mood)
    else:
        st.session_state.selected_sub_moods.add(mood)
    st.rerun()  # keep all selections visually in sync

def clear_all():
    st.session_state.primary_mood = None
    st.session_state.selected_sub_moods.clear()
    st.rerun()
