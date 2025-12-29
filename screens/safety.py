import streamlit as st

def render(on_continue):
    modal = st.empty()

    with modal.container():
        st.markdown("""
        <style>
        .modal-bg {
            position: fixed;
            inset: 0;
            background: rgba(5, 10, 25, 0.75);
            backdrop-filter: blur(12px);
            z-index: 9999;
        }
        .modal-card {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(30, 41, 59, 0.95);
            border-radius: 22px;
            padding: 32px;
            width: 420px;
            color: #e5e7eb;
            box-shadow: 0 25px 60px rgba(0,0,0,0.5);
            z-index: 10000;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="modal-bg"></div>
        <div class="modal-card">
            <h2>We’re here with you 💙</h2>
            <p>
                It sounds like things may feel overwhelming right now.
                Would you like to reach out to someone for support?
            </p>

            <hr style="opacity:0.25">

            <p><strong>Talk to someone right now</strong></p>

            <p>
              🇮🇳 <strong>Kiran (Govt. of India)</strong><br>
              1800-599-0019 · 24/7 · Free
            </p>

            <p>
              🇮🇳 <strong>AASRA</strong><br>
              +91 9820466726 · Confidential
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Yes, show options"):
                st.info("You can call a helpline or contact someone you trust.")

        with col2:
            if st.button("No, continue chatting"):
                modal.empty()
                on_continue()
