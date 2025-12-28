import streamlit as st
from logic.mood_logic import (
    PRIMARY_MOODS,
    init_mood_state,
    set_primary_mood,
    toggle_sub_mood,
    clear_all
)

# ------------------ UI ------------------
def render():
    init_mood_state()

    # ---------- HEADER + SKIP ----------
    col_left, col_right = st.columns([8, 1])

    with col_left:
        st.header("How are you feeling right now?")
        st.caption("Start broad, then be more specific")

    with col_right:
        if st.button("Skip →"):
            st.session_state.current_screen = "Chat"
            st.rerun()

    # ---------- PRIMARY MOODS ----------
    st.subheader("Choose one that fits best")
    cols = st.columns(3)

    for idx, mood in enumerate(PRIMARY_MOODS.keys()):
        with cols[idx % 3]:
            selected = st.session_state.primary_mood == mood

            if st.button(
                mood,
                key=f"primary_{mood}",
                use_container_width=True,
                type="primary" if selected else "secondary"
            ):
                set_primary_mood(mood)

    # ---------- SUB MOODS ----------
    if st.session_state.primary_mood:
        st.subheader("Does any of this match more closely?")
        sub_cols = st.columns(3)

        for idx, sub in enumerate(PRIMARY_MOODS[st.session_state.primary_mood]):
            with sub_cols[idx % 3]:
                is_selected = sub in st.session_state.selected_sub_moods

                if st.button(
                    sub,
                    key=f"sub_{sub}",
                    use_container_width=True,
                    type="primary" if is_selected else "secondary"
                ):
                    toggle_sub_mood(sub)

    st.write("")

    # ---------- ACTIONS ----------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧹 Clear All", use_container_width=True):
            clear_all()
            st.info("Selection cleared")

    with col2:
        if st.button("➡ Continue", use_container_width=True):
            st.success("Mood captured")
