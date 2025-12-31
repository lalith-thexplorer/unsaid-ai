import streamlit as st
from datetime import datetime
from utils import style_utils

# Mood options with emojis
MOODS = [
    {"id": "Anxious", "emoji": "😰", "color": "#A8DADC"},
    {"id": "Calm", "emoji": "😌", "color": "#457B9D"},
    {"id": "Sad", "emoji": "😢", "color": "#1D3557"},
    {"id": "Hopeful", "emoji": "🌟", "color": "#F1FAEE"},
    {"id": "Tired", "emoji": "😴", "color": "#8D99AE"},
    {"id": "Frustrated", "emoji": "😤", "color": "#E63946"},
    {"id": "Grateful", "emoji": "🙏", "color": "#2A9D8F"},
    {"id": "Numb", "emoji": "😶", "color": "#6C757D"},
]

def render():
    style_utils.load_css()
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h2>How are you feeling right now?</h2>
        <p style="opacity: 0.7;">Select all that apply</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize selected moods
    if 'selected_moods' not in st.session_state:
        st.session_state['selected_moods'] = []
    
    # Create mood grid (2 rows of 4)
    cols = st.columns(4)
    
    for i, mood in enumerate(MOODS):
        col_idx = i % 4
        with cols[col_idx]:
            is_selected = mood['id'] in st.session_state['selected_moods']
            
            # Style based on selection
            bg = mood['color'] if is_selected else "rgba(255,255,255,0.05)"
            border = "3px solid #fff" if is_selected else "1px solid rgba(255,255,255,0.1)"
            text_color = "#000" if is_selected else "#fff"
            
            # Mood button (using markdown + button hack)
            st.markdown(f"""
            <div style="
                background: {bg};
                border: {border};
                border-radius: 16px;
                padding: 20px 10px;
                text-align: center;
                margin-bottom: 10px;
                cursor: pointer;
                transition: all 0.2s;
            ">
                <div style="font-size: 2rem;">{mood['emoji']}</div>
                <div style="font-size: 0.9rem; color: {text_color}; margin-top: 5px;">{mood['id']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Actual toggle button
            if st.button(
                "✓" if is_selected else "Select",
                key=f"mood_{mood['id']}",
                use_container_width=True
            ):
                if is_selected:
                    st.session_state['selected_moods'].remove(mood['id'])
                else:
                    st.session_state['selected_moods'].append(mood['id'])
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Show selected moods
    if st.session_state['selected_moods']:
        selected_text = ", ".join(st.session_state['selected_moods'])
        st.info(f"Selected: {selected_text}")
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("⏭️ Skip", use_container_width=True):
            st.session_state['checked_in'] = True
            st.rerun()
    
    with col2:
        if st.button("✅ Continue", use_container_width=True, disabled=not st.session_state['selected_moods']):
            # Save to mood history
            if 'mood_history' not in st.session_state:
                st.session_state['mood_history'] = []
            
            st.session_state['mood_history'].append({
                'timestamp': datetime.now(),
                'moods': st.session_state['selected_moods'].copy()
            })
            
            st.session_state['checked_in'] = True
            st.rerun()
