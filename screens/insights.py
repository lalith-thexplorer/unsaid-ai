import streamlit as st
import streamlit.components.v1 as components
import plotly.express as px
from datetime import datetime
from logic import insights as insights_logic
from utils import style_utils

# Mood Color Mapping
MOOD_COLORS = {
    "Anxious": "#A8DADC", "Calm": "#457B9D", "Sad": "#1D3557",
    "Hopeful": "#F1FAEE", "Tired": "#8D99AE", "Frustrated": "#E63946",
    "Grateful": "#2A9D8F", "Numb": "#6C757D"
}

def render_week_progress(week_data):
    """Renders M T W T F S S progress indicators as simple text."""
    result = ""
    for day in week_data:
        if day['active']:
            result += f"🔵 "  # Active day
        elif day['is_today']:
            result += f"⭕ "  # Today (not yet checked in)
        else:
            result += f"⚫ "  # Inactive
    return result

def render_calendar_grid(weeks, month_name, mood_colors):
    """Renders a simple text-based calendar."""
    # Just return simple text for now
    lines = [f"**{month_name}**", ""]
    lines.append("M  T  W  T  F  S  S")
    
    for week in weeks:
        week_str = ""
        for day_data in week:
            if day_data is None:
                week_str += "   "
            else:
                mood = day_data['mood']
                if mood:
                    # Use colored emoji based on mood type
                    if mood in ["Calm", "Grateful", "Hopeful"]:
                        week_str += "🟢 "
                    elif mood in ["Anxious", "Frustrated"]:
                        week_str += "🔴 "
                    elif mood in ["Sad", "Numb"]:
                        week_str += "🔵 "
                    else:
                        week_str += "🟡 "
                elif day_data['is_today']:
                    week_str += "⭕ "
                else:
                    week_str += "⚫ "
        lines.append(week_str)
    
    return "\n".join(lines)

def render():
    style_utils.load_css()
    
    st.header("Mood Insights")
    st.markdown("<p style='opacity: 0.7; margin-top: -15px; margin-bottom: 30px;'>Your emotional landscape, visualized.</p>", unsafe_allow_html=True)

    # 1. Get Data
    if 'mood_history' not in st.session_state:
        st.session_state['mood_history'] = []

    use_demo_data = st.checkbox("Show Demo Data", value=len(st.session_state['mood_history']) == 0)

    if use_demo_data:
        data = insights_logic.get_dummy_data()
    else:
        data = st.session_state['mood_history']

    if not data:
        st.info("No mood data available yet. Start by checking in!")
        return

    # 2. Process Data
    df = insights_logic.process_mood_data(data)
    
    if df.empty:
        st.warning("Not enough data to generate insights.")
        return

    # =========================================================
    # 3. BENTO GRID - Row 1: Streak, Week Progress, Calendar
    # =========================================================
    col1, col2, col3 = st.columns([1, 1.5, 1.5])
    
    # --- Streak Card (with Fire 🔥) ---
    current_streak = insights_logic.calculate_streak(df)
    with col1:
        st.markdown(f'''
        <div class="bento-card accent-orange" style="text-align: center;">
            <div style="font-size: 2.5rem;">🔥</div>
            <div class="bento-value">{current_streak}</div>
            <div class="bento-label">Day Streak</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # --- Week Progress (M T W T F S S) ---
    week_data = insights_logic.get_week_progress(df)
    with col2:
        style_utils.card_start()
        st.caption("THIS WEEK")
        st.markdown("**M  T  W  T  F  S  S**")
        st.write(render_week_progress(week_data))
        style_utils.card_end()
    
    # --- Monthly Calendar ---
    calendar_weeks, month_name = insights_logic.get_full_calendar_grid(df)
    with col3:
        style_utils.card_start()
        st.markdown(render_calendar_grid(calendar_weeks, month_name, MOOD_COLORS))
        style_utils.card_end()

    # =========================================================
    # 4. BENTO GRID - Row 2: Mood Frequency + Timeline
    # =========================================================
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        style_utils.card_start(delay=0.2)
        st.subheader("Mood Distribution")
        counts_df = insights_logic.get_mood_counts(df)
        if not counts_df.empty:
            fig = px.pie(
                counts_df, 
                names='Mood', 
                values='count',
                color='Mood',
                color_discrete_map=MOOD_COLORS,
                hole=0.4,  # Donut chart
            )
            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", 
                plot_bgcolor="rgba(0,0,0,0)",
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2),
                margin=dict(t=0, b=0, l=0, r=0)
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        style_utils.card_end()
    
    with col_chart2:
        style_utils.card_start(delay=0.3)
        st.subheader("Your Journey")
        fig_timeline = px.scatter(
            df, 
            x='Date', 
            y='Time', 
            color='Mood',
            color_discrete_map=MOOD_COLORS,
            template="plotly_dark",
            size='Count',
            size_max=15
        )
        fig_timeline.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", 
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis_title="", yaxis_title="",
            showlegend=False
        )
        fig_timeline.update_traces(marker=dict(line=dict(width=1, color='rgba(255,255,255,0.2)')))
        st.plotly_chart(fig_timeline, use_container_width=True, config={'displayModeBar': False})
        style_utils.card_end()

    # =========================================================
    # 5. Recent Mood Log (Event List)
    # =========================================================
    style_utils.card_start(delay=0.4)
    st.subheader("Recent Check-ins")
    
    # Show last 5 entries
    recent_data = data[-5:][::-1]  # Last 5, reversed (newest first)
    for entry in recent_data:
        ts = entry['timestamp']
        moods = entry['moods']
        mood_pills = " ".join([f'<span style="background:{MOOD_COLORS.get(m, "#555")}; padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; margin-right: 4px;">{m}</span>' for m in moods])
        st.markdown(f'''
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
            <div>{mood_pills}</div>
            <div style="opacity: 0.6; font-size: 0.8rem;">{ts.strftime('%b %d, %H:%M')}</div>
        </div>
        ''', unsafe_allow_html=True)
    
    style_utils.card_end()

    # 6. Clear Data
    st.markdown("---")
    if st.button("🗑️ Clear My Data"):
        st.session_state['mood_history'] = []
        st.success("Data cleared.")
        st.rerun()
