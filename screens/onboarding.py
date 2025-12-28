import streamlit as st

def render():
    st.header("Welcome to Unsaid")
    st.caption("A space for what you can’t say out loud.")

    st.markdown(
        "Unsaid provides emotional support only and does not offer medical advice or diagnosis."
    )

    st.text_input(
        "Trusted contact (optional)",
        placeholder="Email or contact identifier",
    )

    st.button("Start")
