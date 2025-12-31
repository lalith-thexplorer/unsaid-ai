import streamlit as st
from utils import style_utils

def render():
    style_utils.load_css()
    
    # Center content
    st.markdown("""
    <div style="text-align: center; padding: 60px 20px;">
        <h1 style="font-size: 4rem; margin-bottom: 0;">Unsaid</h1>
        <p style="opacity: 0.7; font-size: 1.2rem; margin-bottom: 40px;">
            A space for what you can't say out loud.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Glass card for content
    style_utils.card_start()
    
    st.markdown("""
    <p style="text-align: center; opacity: 0.8; margin-bottom: 30px;">
        This is a safe, private space for emotional support.<br>
        No judgments. No data stored. Just you.
    </p>
    """, unsafe_allow_html=True)
    
    # Trusted contact input
    trusted_contact = st.text_input(
        "🛡️ Trusted Contact (optional)",
        placeholder="Email or phone of someone you trust",
        key="trusted_contact"
    )
    
    if trusted_contact:
        st.session_state['trusted_contact'] = trusted_contact
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Start button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Begin Your Journey", use_container_width=True):
            st.session_state['onboarded'] = True
            st.rerun()
    
    style_utils.card_end()
    
    # Disclaimer
    st.markdown("""
    <div style="text-align: center; opacity: 0.5; font-size: 0.8rem; margin-top: 40px;">
        ⚠️ Unsaid provides emotional support only.<br>
        It is not a substitute for professional mental health care.
    </div>
    """, unsafe_allow_html=True)
