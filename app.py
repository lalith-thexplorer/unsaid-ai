import streamlit as st

# -------------------------------------------------
# 1. Import Screens
# -------------------------------------------------
from screens.home import render as home_screen
from screens.chat import render as chat_screen
from screens.insights import render as insights_screen

# -------------------------------------------------
# 2. App Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Unsaid",
    page_icon="💬",
    layout="wide",
)

# -------------------------------------------------
# 3. Read page from URL
# -------------------------------------------------
page = st.query_params.get("page", "Home")

# -------------------------------------------------
# 4. Styles + HTML Navbar (NO JS)
# -------------------------------------------------
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: #0f1117;
            color: #ffffff;
        }}

        header {{
            visibility: hidden;
        }}

        /* Smooth page fade-in */
        .main-content {{
            margin-top: {'90px' if page!='Home' else '30px'};
            animation: fadeIn 0.35s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{
                opacity: 0;
                transform: translateY(6px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        /* Floating Glass Navbar */
        .glass-nav {{
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 999999;

            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(22px) saturate(180%);
            -webkit-backdrop-filter: blur(22px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 100px;
            padding: 6px;

            display: {'none' if page=='Home' else 'flex'};
            gap: 6px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.45);
        }}

        /* Nav links — clean, bold, NO glow */
        .nav-link,
        .nav-link:visited,
        .nav-link:active {{
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 26px;
            border-radius: 100px;
            font-weight: 700;          /* slightly bolder */
            font-size: 15px;
            text-decoration: none !important;

            color: #ffffff !important;
            background: transparent;  /* default state */

            transition: background 0.2s ease, border 0.2s ease;
        }}

        /* ✅ CLEAR HOVER STATE (solid grey) */
        .nav-link:hover {{
            background: rgba(120, 120, 120, 0.35);  /* visible grey */
        }}

        /* Active page */
        .nav-link.active {{
            background: rgba(255, 255, 255, 0.18);
            border: 1px solid rgba(255, 255, 255, 0.45);
        }}

        /* SVG icons */
        .nav-icon {{
            width: 16px;
            height: 16px;
            stroke: white;
            stroke-width: 2;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }}
    </style>

    <div class="glass-nav">
        <a class="nav-link {'active' if page=='Home' else ''}" href="?page=Home" target="_self">
            <svg class="nav-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
            Home
        </a>
        <a class="nav-link {'active' if page=='Chat' else ''}" href="?page=Chat" target="_self">
            <svg class="nav-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
            Chat
        </a>
        <a class="nav-link {'active' if page=='Reflection' else ''}" href="?page=Reflection" target="_self">
            <svg class="nav-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
            </svg>
            Reflection
        </a>
    </div>
    """,
    unsafe_allow_html=True
)






# -------------------------------------------------
# 5. Page Router
# -------------------------------------------------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

if page == "Home":
    home_screen()
elif page == "Chat":
    chat_screen()
elif page == "Reflection":
    insights_screen()

st.markdown('</div>', unsafe_allow_html=True)

