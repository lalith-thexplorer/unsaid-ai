import streamlit as st

st.set_page_config(page_title="Glass AI Chat", layout="wide")

def apply_glass_css():
    st.markdown(f"""
    <style>
    /* 1. UNIVERSAL BACKGROUND: Applies to the very bottom layer of the browser */
    html, body, [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
        background-attachment: fixed !important;
    }}

    /* 2. REMOVE STREAMLIT DEFAULT BACKGROUNDS */
    .stApp {{
        background: transparent !important;
    }}

    /* Target the new Streamlit bottom container to be transparent */
    [data-testid="stBottomBlockContainer"] {{
        background-color: transparent !important;
        border: none !important;
    }}

    /* 3. LAYOUT & SPACING */
    [data-testid="stAppViewBlockContainer"] {{
        max-width: 1000px !important;
        padding-bottom: 150px !important; 
    }}

    [data-testid="stVerticalBlock"] > [data-testid="element-container"] {{
        width: 100% !important;
    }}

    /* 4. CHAT BUBBLES */
    .message-row {{
        display: flex;
        width: 100%;
        margin: 5px 0;
    }}
    .user-row {{ justify-content: flex-end; }}
    .bot-row {{ justify-content: flex-start; }}

    .glass-bubble {{
        padding: 12px 18px;
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        max-width: 65%;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }}

    .user-bubble {{
        background: rgba(168, 85, 247, 0.2); 
        border-radius: 20px 20px 4px 20px;
        border: 1px solid rgba(168, 85, 247, 0.3);
    }}

    .bot-bubble {{
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px 20px 20px 4px;
    }}

    /* 5. LIQUID GLASS INPUT FIELD */
    [data-testid="stChatInput"] {{
        background-color: transparent !important;
    }}

    /* The capsule wrapper */
    [data-testid="stChatInput"] > div {{
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(30px) saturate(160%) !important;
        -webkit-backdrop-filter: blur(30px) saturate(160%) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 30px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4) !important;
    }}

    /* Text input transparency */
    [data-testid="stChatInput"] textarea {{
        background-color: transparent !important;
        color: white !important;
    }}

    header, footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

def render():
    apply_glass_css()
    
    st.markdown("<h2 style='text-align: center; color: white; font-weight: 200; letter-spacing: 2px;'>GLASS CHAT</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.1)'>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome. The background should now extend fully behind this input field."}
        ]

    for msg in st.session_state.messages:
        is_user = msg["role"] == "user"
        row_class = "user-row" if is_user else "bot-row"
        bubble_class = "user-bubble" if is_user else "bot-bubble"
        
        st.markdown(f"""
            <div class="message-row {row_class}">
                <div class="glass-bubble {bubble_class}">
                    {msg['content']}
                </div>
            </div>
        """, unsafe_allow_html=True)

    if prompt := st.chat_input("Message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": "The background is now consistent across the whole page."})
        st.rerun()

if __name__ == "__main__":
    render()