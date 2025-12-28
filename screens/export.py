import streamlit as st

def render():
    st.header("Reflection Summary")

    st.markdown(
        """
        **Summary Preview**
        - Recent moods
        - Key reflections
        - Short notes
        """
    )

    st.button("Download PDF")
    st.button("Download HTML")

    st.caption(
        "This summary is not a medical assessment and is intended for personal reflection."
    )
