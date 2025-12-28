import streamlit as st

def render():
    st.header("We’re here to support you")

    st.markdown(
        "It sounds like you might be going through something really difficult."
    )

    st.markdown("**If you’re in immediate danger, please contact local emergency services.**")

    st.markdown("📞 **Helpline:** 988 (example)")

    if st.button("Notify trusted contact"):
        st.info("Trusted contact would be notified (demo behavior).")

    st.button("Continue chatting")
