import streamlit as st
import streamlit.components.v1 as components

def render():
    # Set page config for a cleaner look
    st.set_page_config(page_title="Unsaid", layout="wide")

    # -------------------------------------------------
    # GLOBAL CSS: Total Centering & Glass Theme
    # -------------------------------------------------
    st.markdown("""
        <style>
        /* 1. ROOT OVERRIDES */
        /* Hide Streamlit elements */
        header, footer, [data-testid="stHeader"] { visibility: hidden; height: 0; }
        
        /* Force the main container to fill the screen and center content */
        [data-testid="stAppViewBlockContainer"] {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100vw !important;
            width: 100vw !important;
            height: 100vh !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            overflow: hidden !important;
        }

        /* Target the internal block container that usually forces left-align */
        .main .block-container {
            max-width: 100% !important;
            width: 100% !important;
            padding: 0 !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
        }

        /* 2. BACKGROUND THEME */
        .stApp {
            background: 
                radial-gradient(1200px 800px at 12% 10%, rgba(124,131,253,0.25), transparent 60%),
                radial-gradient(900px 700px at 85% 20%, rgba(168,85,247,0.20), transparent 58%),
                linear-gradient(180deg, #0f1117, #0b0d14);
            overflow: hidden !important;
        }

        /* 3. THE MAIN GLASS SLAB */
        .glass-slab {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(35px) saturate(180%);
            -webkit-backdrop-filter: blur(35px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 50px;
            padding: 60px 40px;
            width: 90vw;
            max-width: 1150px;
            text-align: center;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px;
            margin: auto; /* Fallback centering */
        }

        .title {
            color: white;
            font-size: clamp(2.5rem, 8vw, 4.2rem);
            font-weight: 900;
            margin: 0;
            background: linear-gradient(to bottom, #ffffff, #a855f7);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -2px;
        }

        .subtitle {
            color: #e2e8f0;
            font-size: clamp(1.5rem, 3.5vw, 2rem); 
            
            font-weight: 500;
            
            margin-top: -25px; 
            
            margin-bottom: 15px;
            opacity: 0.6;
            letter-spacing: 0.5px;
            text-shadow: 0 0 25px rgba(168, 85, 247, 0.5);
        }

        /* 4. INFINITE CAROUSEL */
        #infinite-scroll-container {
            display: flex;
            overflow: hidden; 
            gap: 20px;
            padding: 20px 0;
            white-space: nowrap;
            width: 100%;
            mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
        }

        .card {
            min-width: 300px;
            padding: 25px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 35px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            white-space: normal;
        }

        .card:hover {
            transform: scale(1.05) translateY(-5px);
            border-color: #a855f7;
            box-shadow: 0 0 10px rgba(168, 85, 247, 0.15);
            background: rgba(255, 255, 255, 0.08);
        }

        .icon { font-size: 2.2rem; margin-bottom: 12px; }
        .card-title { color: white; font-weight: 800; font-size: 1.2rem; margin-bottom: 6px; }
        .card-desc { color: #94a3b8; font-size: 0.95rem; line-height: 1.4; }

        /* 5. CTA BUTTON */
        /* 5. CTA BUTTON: MATCHING NAVBAR STYLE */
        .btn-link { 
            text-decoration: none !important; 
            margin-top: 15px; 
        }

        .glass-btn {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 14px 40px;
            
            /* Matching your Glass-Nav background & blur */
            background: rgba(255, 255, 255, 0.04);
            backdrop-filter: blur(22px) saturate(180%);
            -webkit-backdrop-filter: blur(22px) saturate(180%);
            
            /* Matching your Navbar active-state border */
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 100px;
            
            color: #ffffff;
            font-size: 16px;
            font-weight: 700; /* Bold like your Nav links */
            cursor: pointer;
            transition: all 0.2s ease;
            letter-spacing: 0.5px;
        }

        /* Hover state matching your .nav-link:hover */
        .glass-btn:hover {
            background: rgba(120, 120, 120, 0.35);
            border: 1px solid rgba(255, 255, 255, 0.45);
            transform: translateY(-2px);
        }

        /* Active click state */
        .glass-btn:active {
            transform: translateY(0);
            background: rgba(255, 255, 255, 0.18);
        }
        </style>
    """, unsafe_allow_html=True)

    # -------------------------------------------------
    # CONTENT STRUCTURE
    # -------------------------------------------------
    features = [
        ("💬", "Anonymous Conversations", "Speak freely without accounts or identity."),
        ("❤️", "Emotion-Aware Chat", "Responses that listen before reacting."),
        ("🛡️", "Private & Secure", "Nothing stored. Everything stays with you."),
        ("🧠", "Reflect & Understand", "See patterns from your conversation."),
        ("🌱", "No Judgement Zone", "No diagnosis. No labels."),
        ("⏳", "Your Pace", "Pause. Resume. Talk when ready."),
    ]
    
    # Triple cards for the infinite loop
    card_html = "".join([
        f'''<div class="card">
            <div class="icon">{icon}</div>
            <div class="card-title">{title}</div>
            <div class="card-desc">{desc}</div>
        </div>''' for icon, title, desc in features
    ] * 3)
    
    st.markdown(f"""
        <div class="glass-slab">
            <div class="title">Unsaid</div>
            <div class="subtitle">A space to talk, without judgement.</div>
            <div id="infinite-scroll-container">
                {card_html}
            </div>
            <a href="?page=Chat" target="_self" class="btn-link">
                <button class="glass-btn">
                    <svg class="nav-icon" viewBox="0 0 24 24" style="width:18px; height:18px; stroke:white; fill:none; stroke-width:2;">
                        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                    </svg>
                    Enter The Space
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------
    # JS: ANIMATION & SCROLL
    # -------------------------------------------------
    components.html("""
        <script>
        const container = window.parent.document.getElementById('infinite-scroll-container');
        let speed = 0.8;
        let paused = false;

        function animate() {
            if (!paused && container) {
                container.scrollLeft += speed;
                if (container.scrollLeft >= (container.scrollWidth / 3)) {
                    container.scrollLeft = 0;
                }
            }
            requestAnimationFrame(animate);
        }

        window.parent.addEventListener('wheel', (e) => {
            if (container) {
                container.scrollLeft += e.deltaY;
            }
        }, { passive: true });

        if (container) {
            container.addEventListener('mouseenter', () => paused = true);
            container.addEventListener('mouseleave', () => paused = false);
        }

        animate();
        </script>
        """, height=0)

if __name__ == "__main__":
    render()