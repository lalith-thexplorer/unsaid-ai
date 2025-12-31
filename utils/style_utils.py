import streamlit as st

def load_css():
    """
    Injects custom CSS for 'Deep Glass' aesthetic.
    Reference: Purple/Blue swirls, heavy blur, screen transitions.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

        /* -------------------------------------------------------------
           1. CORE LAYOUT & ANIMATIONS
        ------------------------------------------------------------- */
        @keyframes gradient-animation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translate3d(0, 40px, 0);
            }
            to {
                opacity: 1;
                transform: translate3d(0, 0, 0);
            }
        }

        /* The Living Background */
        .stApp {
            background-color: #0f0c29;
            background-image: 
                radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
                radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
                radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%), 
                radial-gradient(at 0% 50%, hsla(269, 50%, 40%, 1) 0, transparent 50%), 
                radial-gradient(at 100% 50%, hsla(300, 50%, 30%, 1) 0, transparent 50%), 
                radial-gradient(at 0% 100%, hsla(220, 50%, 30%, 1) 0, transparent 50%), 
                radial-gradient(at 100% 100%, hsla(280, 40%, 30%, 1) 0, transparent 50%);
            background-size: 200% 200%;
            animation: gradient-animation 20s ease infinite; 
            color: #E0E0E0;
            font-family: 'Outfit', sans-serif;
        }
        
        /* Font Overrides */
        h1, h2, h3, p, div, span, button {
            font-family: 'Outfit', sans-serif !important;
        }
        
        /* Remove Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;} 

        /* -------------------------------------------------------------
           2. GLASSMOPHISM CARDS
        ------------------------------------------------------------- */
        .glass-card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-top: 1px solid rgba(255, 255, 255, 0.3);
            border-left: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 24px;
            padding: 30px;
            margin-bottom: 24px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            
            /* Prepare for 3D Motion */
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
            transform-style: preserve-3d;
            perspective: 1000px;
            
            /* Animation Entrance */
            animation: fadeInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) both;
        }
        
        .glass-card:hover {
            border-color: rgba(255, 255, 255, 0.6);
            transform: translateY(-10px) scale(1.02) rotateX(2deg) rotateY(-2deg);
            box-shadow: -20px 20px 50px rgba(0,0,0,0.5), 0 0 20px rgba(100, 100, 255, 0.2);
            z-index: 10;
        }

        /* -------------------------------------------------------------
           3. BENTO GRID WIDGETS
        ------------------------------------------------------------- */
        .bento-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.03));
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 20px;
            text-align: left;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            position: relative;
            overflow: hidden;
            
            /* Entrance */
            animation: fadeInUp 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) both;
        }
        
        .bento-card:hover {
            transform: translateY(-5px) scale(1.02);
            border-color: rgba(255,255,255,0.3);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        
        /* Colored accents */
        .accent-blue { border-left: 4px solid #4da6ff; }
        .accent-orange { border-left: 4px solid #ff9f43; }
        .accent-pink { border-left: 4px solid #ff9ff3; }

        .bento-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            opacity: 0.7;
            margin-bottom: 8px;
        }
        .bento-value {
            font-size: 2.2rem;
            font-weight: 700;
            color: #fff;
        }
        
        /* -------------------------------------------------------------
           4. BUTTONS
        ------------------------------------------------------------- */
        .stButton button {
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.25);
            color: #FFF;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: rgba(255, 255, 255, 0.25);
            border-color: #fff;
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
            transform: scale(1.02);
        }
        
        </style>
    """, unsafe_allow_html=True)

def card_start(delay=0):
    st.markdown(f'<div class="glass-card" style="animation-delay: {delay}s;">', unsafe_allow_html=True)

def card_end():
    st.markdown('</div>', unsafe_allow_html=True)

def metric_card(label, value, color="blue", delay=0):
    """
    Renders a small Bento-style widget.
    color: 'blue', 'orange', or 'pink'
    """
    st.markdown(f"""
    <div class="bento-card accent-{color}" style="animation-delay: {delay}s;">
        <div class="bento-label">{label}</div>
        <div class="bento-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)
