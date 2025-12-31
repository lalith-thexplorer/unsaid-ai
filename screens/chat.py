import streamlit as st
from utils import style_utils
from logic import ai_engine

def render():
    style_utils.load_css()
    
    st.header("💬 Chat")
    st.markdown("<p style='opacity: 0.7; margin-top: -15px;'>I'm here to listen. Share what's on your mind.</p>", unsafe_allow_html=True)
    
    # Initialize chat history
    if 'chat_messages' not in st.session_state:
        st.session_state['chat_messages'] = []
        # Add welcome message
        moods = st.session_state.get('selected_moods', [])
        if moods:
            welcome = f"I see you're feeling {', '.join(moods).lower()}. I'm here for you. What's on your mind?"
        else:
            welcome = "Hello. I'm here whenever you're ready to talk. What would you like to share today?"
        st.session_state['chat_messages'].append({
            'role': 'assistant',
            'content': welcome
        })
    
    # Chat container
    style_utils.card_start()
    
    # Display messages
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state['chat_messages']:
            if msg['role'] == 'user':
                st.markdown(f"""
                <div style="
                    background: rgba(255,255,255,0.1);
                    border-radius: 16px 16px 4px 16px;
                    padding: 12px 16px;
                    margin: 8px 0;
                    margin-left: 20%;
                    text-align: right;
                ">
                    {msg['content']}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="
                    background: rgba(69, 123, 157, 0.3);
                    border-radius: 16px 16px 16px 4px;
                    padding: 12px 16px;
                    margin: 8px 0;
                    margin-right: 20%;
                ">
                    🤖 {msg['content']}
                </div>
                """, unsafe_allow_html=True)
    
    style_utils.card_end()
    
    # Input area
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "Message",
            placeholder="Type your message...",
            label_visibility="collapsed",
            key="chat_input"
        )
    
    with col2:
        send_clicked = st.button("Send", use_container_width=True)
    
    if send_clicked and user_input:
        # Check for crisis
        if ai_engine.detect_crisis(user_input):
            st.session_state['show_safety'] = True
            st.rerun()
        
        # Add user message
        st.session_state['chat_messages'].append({
            'role': 'user',
            'content': user_input
        })
        
        # Get AI response
        moods = st.session_state.get('selected_moods', [])
        response = ai_engine.get_ai_response(user_input, moods)
        
        st.session_state['chat_messages'].append({
            'role': 'assistant',
            'content': response
        })
        
        st.rerun()
    
    # Coping suggestion
    moods = st.session_state.get('selected_moods', [])
    if moods:
        st.markdown("---")
        st.markdown("**💡 Coping Tip:**")
        suggestion = ai_engine.get_coping_suggestion(moods[0])
        st.info(suggestion)
