import streamlit as st


def render(on_continue=None):
    st.markdown(
        """
        <div style="
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.8);
            backdrop-filter: blur(12px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
        ">
            <div style="
                background: #111827;
                color: #e5e7eb;
                padding: 32px;
                border-radius: 18px;
                max-width: 420px;
                text-align: center;
            ">
                <h3>You’re not alone 💙</h3>
                <p>
                    If things feel overwhelming, reaching out right now
                    can really help.
                </p>

                <p><strong>India – KIRAN</strong><br>1800-599-0019 (24/7)</p>

                <p style="font-size:12px; opacity:0.6">
                    This is not a medical service.<br>
                    No action is taken without your consent.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Continue chatting"):
            st.session_state.show_safety_overlay = False
            if on_continue:
                on_continue()

    with col2:
        if st.button("Notify trusted contact"):
            st.info("Demo only – no real action taken.")
