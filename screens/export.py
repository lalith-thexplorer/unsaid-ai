import streamlit as st
from datetime import datetime
from logic import export as export_logic
from logic import insights as insights_logic
from utils import style_utils

# Mood colors for display
MOOD_COLORS = {
    "Anxious": "#A8DADC", "Calm": "#457B9D", "Sad": "#1D3557",
    "Hopeful": "#F1FAEE", "Tired": "#8D99AE", "Frustrated": "#E63946",
    "Grateful": "#2A9D8F", "Numb": "#6C757D"
}

def render():
    style_utils.load_css()
    
    st.header("📄 Reflection Export")
    st.markdown("<p style='opacity: 0.7; margin-top: -15px;'>Download a summary of your emotional journey.</p>", unsafe_allow_html=True)
    
    # Get data
    mood_history = st.session_state.get('mood_history', [])
    
    if not mood_history:
        style_utils.card_start()
        st.info("No mood data to export yet. Start by checking in!")
        style_utils.card_end()
        return
    
    # Stats row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        style_utils.metric_card("Total Check-ins", str(len(mood_history)), color="blue")
    
    with col2:
        # Calculate streak
        df = insights_logic.process_mood_data(mood_history)
        streak = insights_logic.calculate_streak(df) if not df.empty else 0
        style_utils.metric_card("Current Streak", f"{streak} days", color="orange")
    
    with col3:
        # Most common mood
        if not df.empty:
            top_mood = df['Mood'].mode()[0]
        else:
            top_mood = "N/A"
        style_utils.metric_card("Top Mood", top_mood, color="pink")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Preview section
    style_utils.card_start()
    st.subheader("📋 Preview")
    
    # Recent entries
    recent = mood_history[-5:][::-1]
    for entry in recent:
        ts = entry['timestamp']
        moods = entry['moods']
        mood_pills = " ".join([f"**{m}**" for m in moods])
        st.markdown(f"• {ts.strftime('%b %d, %H:%M')} — {mood_pills}")
    
    if len(mood_history) > 5:
        st.caption(f"...and {len(mood_history) - 5} more entries")
    
    style_utils.card_end()
    
    # Notes section
    style_utils.card_start()
    st.subheader("📝 Personal Notes")
    notes = st.text_area(
        "Add any reflections you want to include in your export:",
        placeholder="What did you learn about yourself today?",
        height=100,
        key="export_notes"
    )
    style_utils.card_end()
    
    # Download section
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Generate PDF
        pdf_data = export_logic.generate_pdf_report(mood_history, notes or "")
        st.download_button(
            label="📥 Download PDF",
            data=pdf_data,
            file_name=f"unsaid_reflection_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    with col2:
        if st.button("🗑️ Clear All Data", use_container_width=True):
            st.session_state['mood_history'] = []
            st.session_state['chat_messages'] = []
            st.session_state['selected_moods'] = []
            st.success("All data cleared!")
            st.rerun()
    
    # Disclaimer
    st.markdown("""
    <div style="text-align: center; opacity: 0.5; font-size: 0.8rem; margin-top: 30px;">
        ⚠️ This export is for personal reflection only. It is not a medical document.
    </div>
    """, unsafe_allow_html=True)
