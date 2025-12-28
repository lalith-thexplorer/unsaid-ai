import streamlit as st

def render():
    st.header("Chat")

    st.write("This is where the empathetic AI chat will live.")

    user_input = st.text_input("Type your message here")

    if st.button("Send"):
        if user_input:
            st.write("🧑 You:", user_input)
            st.write("🤖 AI:", "I’m here with you. Tell me more.")
        else:
            st.warning("Please enter a message.")
