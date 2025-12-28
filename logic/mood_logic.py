import streamlit as st

PRIMARY_MOODS = {

    # ---------------- POSITIVE / LIGHT ----------------
    "😊 Happy": [
        "😄 Excited",
        "🫶 Grateful",
        "😌 Calm",
        "💪 Motivated",
        "😇 Content",
        "🤗 Loved",
        "✨ Optimistic",
        "🥰 Warm",
        "😎 Confident"
    ],

    "🌈 Hopeful": [
        "✨ Optimistic",
        "🌱 Growing",
        "🛤️ Looking forward",
        "🙏 Trusting",
        "🤍 Encouraged",
        "🕊️ Peaceful hope",
        "💭 Dreaming",
        "🌅 Renewed"
    ],

    "🤩 Energized": [
        "⚡ Alert",
        "🔥 Inspired",
        "🚀 Driven",
        "🎯 Focused",
        "😃 Enthusiastic",
        "💥 Pumped",
        "🧠 Sharp",
        "🏃 Ready to act"
    ],

    # ---------------- NEUTRAL / FLAT ----------------
    "😐 Neutral": [
        "😶 Numb",
        "😑 Meh",
        "🤔 Thoughtful",
        "🧠 Reflective",
        "😌 Okay",
        "🫥 Blank",
        "😴 Indifferent",
        "🤷 Unbothered"
    ],

    "🤔 Confused": [
        "😕 Unsure",
        "🫠 Mixed feelings",
        "😵 Overthinking",
        "🤷 Lost",
        "🧩 Unclear",
        "😬 Awkward",
        "🌀 Scattered"
    ],

    # ---------------- HEAVY / NEGATIVE ----------------
    "😔 Sad": [
        "😢 Lonely",
        "💔 Hurt",
        "😞 Low",
        "😥 Disappointed",
        "🥀 Empty",
        "😓 Tearful",
        "😟 Hopeless",
        "🫤 Down"
    ],

    "⚡ Anxious": [
        "😰 Stressed",
        "😬 Nervous",
        "🤯 Overwhelmed",
        "🫨 On edge",
        "😟 Worried",
        "⏳ Restless",
        "🧠 Racing thoughts",
        "🫥 Uneasy"
    ],

    "😡 Angry": [
        "😠 Irritated",
        "😤 Frustrated",
        "🤬 Furious",
        "😒 Annoyed",
        "🔥 Heated",
        "💢 Agitated",
        "😑 Fed up",
        "🧨 Resentful"
    ],

    # ---------------- ENERGY / LOAD ----------------
    "😴 Tired": [
        "🥱 Sleepy",
        "🪫 Drained",
        "😩 Exhausted",
        "😓 Worn out",
        "🧠 Mentally tired",
        "🛌 Need rest",
        "😵 Fatigued",
        "📉 Low energy"
    ],

    "😞 Stressed": [
        "📚 Overloaded",
        "⏰ Pressured",
        "🧠 Mentally cluttered",
        "😖 Tense",
        "😥 Anxious-stress",
        "🫠 Near burnout",
        "😓 Burned out",
        "🔒 Trapped"
    ],

    # ---------------- OTHER / MIXED ----------------
    "🌧️ Other": [
        "😶 Conflicted",
        "🤩 Inspired",
        "🥳 Playful",
        "😳 Embarrassed",
        "😬 Awkward",
        "🤷 Unsure",
        "🫠 Mixed emotions",
        "🧘 Detached"
    ]
}


def init_mood_state():
    if "primary_mood" not in st.session_state:
        st.session_state.primary_mood = None
    if "selected_sub_moods" not in st.session_state:
        st.session_state.selected_sub_moods = set()

def set_primary_mood(mood):
    st.session_state.primary_mood = mood
    st.session_state.selected_sub_moods.clear()
    st.rerun()

def toggle_sub_mood(mood):
    if mood in st.session_state.selected_sub_moods:
        st.session_state.selected_sub_moods.remove(mood)
    else:
        st.session_state.selected_sub_moods.add(mood)
    st.rerun()

def clear_all():
    st.session_state.primary_mood = None
    st.session_state.selected_sub_moods.clear()
    st.rerun()
