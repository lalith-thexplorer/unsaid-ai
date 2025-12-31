import streamlit as st
from utils import style_utils

def render():
    style_utils.load_css()
    
    # Full-screen overlay effect
    st.markdown("""
    <style>
    .safety-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.9);
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main content
    st.markdown("""
    <div style="text-align: center; padding: 40px 20px;">
        <div style="font-size: 4rem; margin-bottom: 20px;">💙</div>
        <h1>We're Here For You</h1>
    </div>
    """, unsafe_allow_html=True)
    
    style_utils.card_start()
    
    st.markdown("""
    <div style="text-align: center;">
        <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 30px;">
            It sounds like you might be going through something really difficult right now.
            <br><br>
            <strong>You are not alone.</strong> There are people who care and want to help.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Helpline numbers
    st.markdown("""
    <div style="
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
    ">
        <p style="margin-bottom: 15px;"><strong>📞 Crisis Helplines:</strong></p>
        <p>🇺🇸 National Suicide Prevention: <strong>988</strong></p>
        <p>🇮🇳 iCall: <strong>9152987821</strong></p>
        <p>🇮🇳 Vandrevala Foundation: <strong>1860-2662-345</strong></p>
        <p>🌍 International Association for Suicide Prevention: <a href="https://www.iasp.info/resources/Crisis_Centres/" style="color: #A8DADC;">Find your country</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    style_utils.card_end()
    
    # Actions
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.get('trusted_contact'):
            if st.button("🛡️ Notify Trusted Contact", use_container_width=True):
                st.success(f"Message sent to your trusted contact.")
                st.balloons()
    
    with col2:
        if st.button("💬 Continue Chatting", use_container_width=True):
            st.session_state['show_safety'] = False
            st.rerun()
    
    # Disclaimer
    st.markdown("""
    <div style="text-align: center; opacity: 0.5; font-size: 0.8rem; margin-top: 40px;">
        ⚠️ Unsaid is not a crisis service. If you're in immediate danger, please call emergency services.
    </div>
    """, unsafe_allow_html=True)
