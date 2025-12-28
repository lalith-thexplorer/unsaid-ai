import streamlit as st

def render():
    # Fixed CSS - UI Guidelines compliant
    st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2a 50%, #1e1e3a 100%);
            min-height: 100vh;
        }
        .main-card {
            background: rgba(30, 30, 46, 0.7);
            backdrop-filter: blur(20px);
            border-radius: 24px;
            border: 1px solid rgba(71, 71, 99, 0.4);
            padding: 3rem 2rem;
            max-width: 480px;
            margin: 2rem auto;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }
        .title { color: #f8fafc; font-size: 2.8rem; font-weight: 500; text-align: center; margin-bottom: 0.5rem; }
        .tagline { color: #cbd5e1; font-size: 1.15rem; text-align: center; margin-bottom: 2rem; line-height: 1.6; }
        .mood-row { display: flex; justify-content: center; gap: 1rem; margin: 2rem 0; flex-wrap: wrap; }
        .mood-emoji { 
            font-size: 2.2rem; 
            padding: 1rem; 
            background: rgba(71, 71, 99, 0.3); 
            border-radius: 16px; 
            border: 1px solid rgba(148, 163, 184, 0.3);
            transition: all 0.3s ease;
        }
        .mood-emoji:hover { 
            background: rgba(99, 102, 241, 0.2); 
            border-color: rgba(99, 102, 241, 0.5);
            transform: scale(1.05);
        }
        .btn-primary {
            background: linear-gradient(135deg, #6366f1, #7c3aed);
            border-radius: 16px;
            font-size: 1.1rem;
            font-weight: 500;
            border: none;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True)

    # ✅ FIXED: Proper Streamlit containers that render correctly
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # Title & Tagline
    st.markdown('<h1 class="title">Unsaid</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">A space for what you can\'t say out loud.</p>', unsafe_allow_html=True)
    
    # ✅ FIXED: Mood emojis using st.columns (renders perfectly)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.markdown('<div class="mood-emoji" title="Sad">😔</div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="mood-emoji" title="Worried">😟</div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="mood-emoji" title="Neutral">😐</div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="mood-emoji" title="Happy">😊</div>', unsafe_allow_html=True)
    with col5: st.markdown('<div class="mood-emoji" title="Loved">🥰</div>', unsafe_allow_html=True)
    
    # Disclaimer
    st.info("🛡️ Unsaid provides emotional support only and does not offer medical advice or diagnosis.")
    
    # Trusted contact
    trusted_contact = st.text_input(
        "👤 Trusted contact (optional)", 
        placeholder="Email or phone for crisis support only",
        key="trusted_contact"
    )
    
    # Start button
    if st.button("🌙 Begin", type="primary", key="start"):
        st.session_state.trusted_contact = trusted_contact
        if "page" not in st.session_state:
            st.session_state.page = "mood_checkin"
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(
        "<p style='text-align: center; color: #64748b; font-size: 0.85rem; margin-top: 2rem;'>"
        "💾 Everything stays private on your device"
        "</p>", unsafe_allow_html=True
    )
